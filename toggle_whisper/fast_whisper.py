#!/usr/bin/env python3
"""
Fast Whisper Transcription
--------------------------
Real-time audio transcription using Insanely Fast Whisper for maximum performance.
This implementation is optimized for speed, particularly for English language.

Author: Robert Kubis (https://github.com/h3x89)
"""

import argparse
import json
import logging
import numpy as np
import os
import platform
import pyaudio
import pyperclip
import queue
import subprocess
import sys
import tempfile
import threading
import time
import torch

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("fast_whisper")

# Constants
SAMPLE_RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paFloat32
CHUNK_SIZE = 1024
SILENCE_THRESHOLD = 0.01
MIN_SILENCE_DURATION = 0.7  # Seconds
BUFFER_SIZE = int(SAMPLE_RATE * 30.0)  # 30 seconds buffer

class SilenceDetector:
    """Adaptive silence detection with dynamic thresholding"""
    
    def __init__(self, threshold: float = 0.01, window_size: int = 16000):
        self.base_threshold = threshold
        self.window_size = window_size
        self.noise_levels = np.zeros(window_size)
        self.pointer = 0
        self.current_threshold = threshold

    def is_silent(self, audio_chunk: np.ndarray) -> bool:
        rms = np.sqrt(np.mean(audio_chunk**2))
        self.update_threshold(rms)
        return rms < self.current_threshold

    def update_threshold(self, current_rms: float):
        self.noise_levels[self.pointer] = current_rms
        self.pointer = (self.pointer + 1) % self.window_size
        
        # Dynamic threshold adaptation
        noise_floor = np.percentile(self.noise_levels[self.noise_levels > 0], 25)
        self.current_threshold = max(self.base_threshold, noise_floor * 1.2)

class ClipboardManager:
    """Thread-safe clipboard management with history"""
    
    def __init__(self, max_history: int = 10):
        self.lock = threading.Lock()
        self.history = []
        self.max_history = max_history

    def update(self, text: str):
        with self.lock:
            self.history.append(text)
            if len(self.history) > self.max_history:
                self.history.pop(0)
            full_text = " ".join(self.history)
            pyperclip.copy(full_text)

    def clear(self):
        with self.lock:
            self.history.clear()
            pyperclip.copy("")

class AudioTranscriber:
    def __init__(self, model_size="small", language=None, batch_size=2, debug=False):
        self.model_size = model_size
        self.language = language
        self.batch_size = batch_size
        self.debug = debug
        self.is_recording = False
        self.is_processing = False
        self.audio_queue = queue.Queue()
        self.silence_detector = SilenceDetector(threshold=SILENCE_THRESHOLD)
        self.clipboard = ClipboardManager()
        
        # Check if insanely-fast-whisper is installed
        try:
            import importlib.util
            if importlib.util.find_spec("insanely_fast_whisper") is None:
                logger.error("insanely-fast-whisper is not installed. Please install it with: pip install insanely-fast-whisper")
                sys.exit(1)
        except ImportError:
            logger.error("Failed to check for insanely-fast-whisper. Please install it with: pip install insanely-fast-whisper")
            sys.exit(1)
        
        # Check if the command works
        try:
            result = subprocess.run(["insanely-fast-whisper", "--help"], capture_output=True, text=True)
            if result.returncode != 0:
                logger.error(f"insanely-fast-whisper command not working: {result.stderr}")
                sys.exit(1)
        except Exception as e:
            logger.error(f"insanely-fast-whisper command not working: {e}")
            sys.exit(1)
        
        logger.info(f"Initializing Fast Whisper with model: {model_size}")
        logger.info(f"Language: {language if language else 'auto-detect'}")
        logger.info(f"Batch size: {batch_size}")
        
        # Initialize PyAudio
        self.audio = pyaudio.PyAudio()
        self.stream = None
        
        # Print initial status for Raycast
        print("⚡ Fast Whisper is ready!")
        print(f"Using model: {model_size}")
        print("Listening for audio...")

    def start_recording(self):
        """Start recording audio from the microphone"""
        logger.info("Starting audio recording...")
        self.is_recording = True
        self.stream = self.audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=SAMPLE_RATE,
            input=True,
            frames_per_buffer=CHUNK_SIZE,
            stream_callback=self._audio_callback
        )
        self.stream.start_stream()
        logger.info("Audio recording started")

    def _audio_callback(self, in_data, frame_count, time_info, status):
        """Process audio data from the microphone"""
        if status:
            logger.warning(f"Audio callback status: {status}")
        
        # Convert audio data to numpy array
        audio_data = np.frombuffer(in_data, dtype=np.float32)
        self.audio_queue.put(audio_data)
        return (in_data, pyaudio.paContinue)

    def process_audio(self):
        """Process audio data from the queue"""
        logger.info("Starting audio processing thread")
        self.is_processing = True
        buffer = np.array([], dtype=np.float32)
        silence_counter = 0
        
        while self.is_recording or not self.audio_queue.empty():
            try:
                audio_chunk = self.audio_queue.get(timeout=1.0)
                buffer = np.concatenate((buffer, audio_chunk))
                
                # Check for silence
                if self.silence_detector.is_silent(audio_chunk):
                    silence_counter += 1
                else:
                    silence_counter = 0
                
                # Process if silence detected or buffer too large
                silence_duration = silence_counter * CHUNK_SIZE / SAMPLE_RATE
                if silence_duration >= MIN_SILENCE_DURATION or len(buffer) >= SAMPLE_RATE * 30:
                    if len(buffer) > SAMPLE_RATE:  # At least 1 second of audio
                        self._transcribe_audio(buffer)
                        buffer = np.array([], dtype=np.float32)
                        silence_counter = 0
            except queue.Empty:
                continue
            except Exception as e:
                logger.error(f"Error processing audio: {e}")
                continue
        
        self.is_processing = False
        logger.info("Audio processing thread stopped")

    def _transcribe_audio(self, audio_data, temp_wav_file="temp_audio.wav", temp_json_file="temp_output.json"):
        """Transcribe audio data using Insanely Fast Whisper"""
        start_time = time.time()
        logger.info("Transcribing audio...")
        
        try:
            # Save audio data to a temporary WAV file
            import wave
            import struct
            with wave.open(temp_wav_file, "wb") as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(2)  # 16-bit
                wf.setframerate(SAMPLE_RATE)
                # Convert float32 to int16
                audio_data_int = (audio_data * 32767).astype(np.int16)
                wf.writeframes(audio_data_int.tobytes())
            
            # Build the command for Insanely Fast Whisper
            cmd = [
                "insanely-fast-whisper",
                "--file-name", temp_wav_file,
                "--output-json", temp_json_file,
                "--model-name", f"openai/whisper-{self.model_size}",
                "--batch-size", str(self.batch_size),
                "--flash-attention", str(self.flash_attention),
                "--compute-type", "float16",
                "--beam-size", "5"
            ]
            
            # Add language parameter if specified
            if self.language:
                cmd.extend(["--language", self.language])
            
            # Run the command
            import subprocess
            logger.debug(f"Running command: {' '.join(cmd)}")
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                logger.error(f"Command failed with return code {process.returncode}")
                logger.error(f"STDERR: {stderr}")
                raise Exception(f"Transcription command failed: {stderr}")
            
            # Parse the output
            import json
            try:
                with open(temp_json_file, 'r') as f:
                    result = json.load(f)
                transcript = result.get('text', '')
            except (json.JSONDecodeError, FileNotFoundError) as e:
                logger.error(f"Error parsing JSON output: {e}")
                raise Exception(f"Failed to parse transcription output: {e}")
            
            if transcript:
                self.clipboard.update(transcript)
                # Formatowanie przyjazne dla Raycast
                print("\n-----------------------------------------")
                print(f"Transkrypcja: {transcript}")
                print("-----------------------------------------")
                # Dodatkowa informacja o skopiowaniu do schowka
                print("✅ Tekst został skopiowany do schowka.")
                # Wymuszenie natychmiastowego pokazania wyjścia
                sys.stdout.flush()
            
            # Clean up temporary files
            try:
                os.remove(temp_wav_file)
                os.remove(temp_json_file)
            except OSError as e:
                logger.warning(f"Error removing temporary files: {e}")
            
            processing_time = time.time() - start_time
            logger.info(f"Transcription completed in {processing_time:.2f} seconds")
            
        except Exception as e:
            logger.error(f"Transcription error: {e}")
            # Wyświetl błąd również w standardowym wyjściu dla widoczności w Raycast
            print(f"❌ Błąd transkrypcji: {e}")
            sys.stdout.flush()

    def stop(self):
        """Stop recording and processing"""
        logger.info("Stopping audio recording and processing...")
        self.is_recording = False
        
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        
        self.audio.terminate()
        logger.info("Audio recording stopped")

def main():
    """Main function to run the transcriber"""
    parser = argparse.ArgumentParser(description="Real-time audio transcription using Insanely Fast Whisper")
    parser.add_argument("--model", type=str, default="small", choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper model size (default: small)")
    parser.add_argument("--language", type=str, default=None,
                        help="Language code (default: auto-detect)")
    parser.add_argument("--batch-size", type=int, default=2,
                        help="Batch size for transcription (default: 2)")
    parser.add_argument("--debug", action="store_true",
                        help="Enable debug logging")

    args = parser.parse_args()
    
    # Configure logging level
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging enabled")
    
    # Log system information
    logger.info(f"Python version: {platform.python_version()}")
    logger.info(f"PyAudio version: {pyaudio.__version__}")
    logger.info(f"Torch version: {torch.__version__}")
    logger.info(f"CPU cores: {os.cpu_count()}")
    if torch.cuda.is_available():
        logger.info(f"CUDA available: {torch.cuda.get_device_name(0)}")
    else:
        logger.info("CUDA not available")
    
    try:
        # Create and start the transcriber
        transcriber = AudioTranscriber(
            model_size=args.model,
            language=args.language,
            batch_size=args.batch_size,
            debug=args.debug
        )
        
        # Start recording and processing
        transcriber.start_recording()
        
        # Start processing in a separate thread
        processing_thread = threading.Thread(target=transcriber.process_audio)
        processing_thread.daemon = True
        processing_thread.start()
        
        print("Press Ctrl+C to stop")
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nStopping transcription...")
        finally:
            transcriber.stop()
            processing_thread.join(timeout=2.0)
            logger.info("Transcription service stopped")
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main() 