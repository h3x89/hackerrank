#!/usr/bin/env python3
"""
Polish Whisper Transcription
----------------------------
Real-time audio transcription optimized for Polish language using OpenAI's Whisper model.
This implementation is specifically tuned for better Polish language recognition.

Author: Robert Kubis (https://github.com/h3x89)
"""

import argparse
import logging
import numpy as np
import os
import platform
import pyaudio
import pyperclip
import queue
import sys
import threading
import time
import torch
from faster_whisper import WhisperModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("polish_whisper")

# Constants
SAMPLE_RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paFloat32
CHUNK_SIZE = 1024
SILENCE_THRESHOLD = 0.01
MIN_SILENCE_DURATION = 0.7  # Seconds, adjusted for Polish
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
    def __init__(self, model_size="small", language="pl", use_gpu=True, num_workers=4, debug=False):
        self.model_size = model_size
        self.language = language
        self.use_gpu = use_gpu
        self.num_workers = num_workers
        self.debug = debug
        self.audio_buffer = np.zeros(BUFFER_SIZE, dtype=np.float32)
        self.buffer_index = 0
        self.is_recording = False
        self.is_processing = False
        self.audio_queue = queue.Queue()
        self.silence_detector = SilenceDetector(threshold=SILENCE_THRESHOLD)
        self.clipboard = ClipboardManager()
        self.device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
        
        logger.info(f"Initializing Whisper model: {model_size} (Polish-optimized)")
        logger.info(f"Using device: {self.device}")
        logger.info(f"Language: {language if language else 'auto-detect'}")
        
        # Initialize the model with Polish-optimized parameters
        compute_type = "float32"  # Changed to float32 for better compatibility
        self.model = WhisperModel(
            model_size, 
            device=self.device, 
            compute_type=compute_type,
            cpu_threads=self.num_workers,
            download_root=None
        )
        
        logger.info("Model initialized successfully")
        
        # Initialize PyAudio
        self.audio = pyaudio.PyAudio()
        self.stream = None
        
        # Print initial status for Raycast
        print("🎤 Polish Whisper is ready!")
        print(f"Using model: {model_size} on {self.device}")
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

    def _transcribe_audio(self, audio_data):
        """Transcribe audio data using Whisper"""
        start_time = time.time()
        logger.info("Transcribing audio...")
        
        try:
            # Polish-optimized transcription parameters
            segments, info = self.model.transcribe(
                audio_data, 
                language=self.language if self.language else None,
                beam_size=5,
                vad_filter=True,
                vad_parameters={"threshold": 0.5, "min_silence_duration_ms": 500, "speech_pad_ms": 400},
                task="transcribe"
            )
            
            # Process segments
            transcript = " ".join(segment.text for segment in segments)
            transcript = transcript.strip()
            
            if transcript:
                self.clipboard.update(transcript)
                # Prosta linia separatora zamiast znaków = dla lepszej czytelności w Raycast
                print("\n-----------------------------------------")
                print(f"Transkrypcja: {transcript}")
                print("-----------------------------------------")
                # Dodatkowa informacja o skopiowaniu do schowka
                print("✅ Tekst został skopiowany do schowka.")
                # Wymuszenie natychmiastowego pokazania wyjścia
                sys.stdout.flush()
            
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
    parser = argparse.ArgumentParser(description="Real-time audio transcription optimized for Polish using Whisper")
    parser.add_argument("--model", type=str, default="small", choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper model size (default: small)")
    parser.add_argument("--language", type=str, default="pl",
                        help="Language code (default: pl for Polish)")
    parser.add_argument("--auto-detect", action="store_true",
                        help="Enable automatic language detection")
    parser.add_argument("--no-gpu", action="store_true",
                        help="Disable GPU acceleration")
    parser.add_argument("--cpu_threads", type=int, default=4,
                        help="Number of CPU threads to use (default: 4)")
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
    
    # Handle language setting
    language = None
    if args.auto_detect:
        logger.info("Using automatic language detection")
    else:
        language = args.language
        logger.info(f"Using specified language: {language}")
    
    # Create and start the transcriber
    transcriber = AudioTranscriber(
        model_size=args.model,
        language=language,
        use_gpu=not args.no_gpu,
        num_workers=args.cpu_threads,
        debug=args.debug
    )
    
    # Start recording and processing
    transcriber.start_recording()
    
    # Start processing in a separate thread
    processing_thread = threading.Thread(target=transcriber.process_audio)
    processing_thread.daemon = True
    processing_thread.start()
    
    try:
        logger.info("Press Ctrl+C to stop")
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received")
    finally:
        transcriber.stop()
        logger.info("Waiting for processing to complete...")
        processing_thread.join(timeout=2.0)
        logger.info("Transcription service stopped")

if __name__ == "__main__":
    main() 