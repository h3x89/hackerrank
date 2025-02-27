#!/usr/bin/env python3
"""
Real-time Whisper Transcription System
------------------------------------
An optimized implementation of real-time audio transcription using OpenAI's Whisper model.
Designed for integration with Raycast and system clipboard.

Features:
- Real-time audio streaming with adaptive buffering
- GPU acceleration support
- Automatic silence detection
- Clipboard integration
- Low-latency processing
"""

import os
import sys
import time
import queue
import threading
import numpy as np
import pyaudio
import torch
import pyperclip
import logging
import gc
import platform
import multiprocessing
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from faster_whisper import WhisperModel

# Configure logging
# DEBUG for detailed output
# INFO for normal output
# ERROR for critical errors
# WARNING for warnings only
# CRITICAL for critical errors only

logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class AudioConfig:
    """Audio configuration parameters"""
    CHANNELS: int = 1
    RATE: int = 16000
    CHUNK: int = 1024
    FORMAT: int = pyaudio.paFloat32
    SILENCE_THRESHOLD: float = 0.01
    SILENCE_DURATION: float = 0.7  # seconds
    MAX_BUFFER_SECONDS: int = 30   # Maximum buffer size in seconds
    MIN_BUFFER_SECONDS: int = 1    # Minimum buffer size in seconds

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
        self.history: List[str] = []
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

class WhisperRealtime:
    """Real-time audio transcription using Whisper"""
    
    def __init__(self, model_size: str = "small", language: str = "en", 
                 use_gpu: bool = True, auto_detect: bool = True, num_workers: int = 4):
        self.config = AudioConfig()
        self.audio_queue = queue.Queue()
        self.running = False
        self.silence_detector = SilenceDetector(
            threshold=self.config.SILENCE_THRESHOLD
        )
        self.clipboard = ClipboardManager()
        self.auto_detect = auto_detect
        self.num_workers = num_workers
        
        # Determine compute device
        device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
        
        # Use float32 for better compatibility
        compute_type = "float32"
        
        logger.info(f"Using device: {device}, compute_type: {compute_type}")
        
        # Initialize Whisper model
        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type,
            download_root=None,
            cpu_threads=self.num_workers
        )
        
        # Audio interface
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.language = language
        
        # Print initial status for Raycast
        print("🎤 Whisper is ready!")
        print(f"Using model: {model_size} on {device} ({compute_type})")
        print("Listening for audio...")

    def audio_callback(self, in_data, frame_count, time_info, status):
        """Process incoming audio data"""
        audio_data = np.frombuffer(in_data, dtype=np.float32)
        self.audio_queue.put(audio_data)
        return (in_data, pyaudio.paContinue)

    def process_audio(self):
        """Process audio from queue and perform transcription"""
        buffer = np.array([], dtype=np.float32)
        silence_counter = 0
        
        while self.running:
            try:
                audio_chunk = self.audio_queue.get(timeout=1.0)
                buffer = np.concatenate((buffer, audio_chunk))
                
                # Check for silence
                if self.silence_detector.is_silent(audio_chunk):
                    silence_counter += 1
                else:
                    silence_counter = 0
                
                # Process if silence detected or buffer too large
                if (silence_counter * self.config.CHUNK / self.config.RATE >= 
                    self.config.SILENCE_DURATION) or len(buffer) >= self.config.RATE * 30:
                    
                    if len(buffer) > 0:
                        self._transcribe_audio(buffer)
                        
                        # Reset for next utterance
                        buffer = np.array([], dtype=np.float32)
                        silence_counter = 0
                        
                        # Free memory
                        gc.collect()
                        if torch.cuda.is_available():
                            torch.cuda.empty_cache()
            
            except queue.Empty:
                continue
            except Exception as e:
                logger.error(f"Error in audio processing: {str(e)}", exc_info=True)
                continue

    def _transcribe_audio(self, audio_data):
        """Transcribe audio data using Whisper"""
        start_time = time.time()
        logger.info("Transcribing audio...")
        
        try:
            # Transcribe with standard parameters
            segments, info = self.model.transcribe(
                audio_data, 
                language=self.language if self.language else None,
                beam_size=4,
                vad_filter=True,
                vad_parameters={"threshold": 0.5}
            )
            
            # Process segments
            transcript = " ".join(segment.text for segment in segments)
            transcript = transcript.strip()
            
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
            
            processing_time = time.time() - start_time
            logger.info(f"Transcription completed in {processing_time:.2f} seconds")
            
        except Exception as e:
            logger.error(f"Transcription error: {e}")
            # Wyświetl błąd również w standardowym wyjściu dla widoczności w Raycast
            print(f"❌ Błąd transkrypcji: {e}")
            sys.stdout.flush()

    def start(self):
        """Start the transcription system"""
        # Start recording
        self.running = True
        self.stream = self.audio.open(
            format=self.config.FORMAT,
            channels=self.config.CHANNELS,
            rate=self.config.RATE,
            input=True,
            frames_per_buffer=self.config.CHUNK,
            stream_callback=self.audio_callback
        )
        
        # Start processing thread
        self.process_thread = threading.Thread(target=self.process_audio)
        self.process_thread.daemon = True
        self.process_thread.start()
        
        print("Whisper is listening...", flush=True)
        sys.stdout.flush()

    def stop(self):
        """Stop the transcription system"""
        self.running = False
        if hasattr(self, 'process_thread'):
            self.process_thread.join(timeout=2.0)
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()
        print("Transcription stopped", flush=True)
        sys.stdout.flush()

def main():
    """Main entry point"""
    import argparse
    parser = argparse.ArgumentParser(description="Real-time Whisper Transcription")
    parser.add_argument("--model", default="small", help="Whisper model size (tiny, base, small, medium)")
    parser.add_argument("--language", default="en", help="Language code (ignored if --auto-detect is used)")
    parser.add_argument("--no-gpu", action="store_true", help="Disable GPU acceleration")
    parser.add_argument("--auto-detect", action="store_true", help="Enable automatic language detection")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--cpu_threads", type=int, default=4, help="Number of CPU threads to use")
    args = parser.parse_args()

    # Set logging level
    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    try:
        # Log system information
        logger.info("Starting whisper_realtime.py")
        logger.info(f"Python version: {sys.version}")
        logger.info(f"PyAudio version: {pyaudio.__version__}")
        logger.info(f"Torch version: {torch.__version__}")
        logger.info(f"CUDA available: {torch.cuda.is_available()}")
        logger.info(f"System: {platform.system()} {platform.release()} ({platform.processor()})")
        logger.info(f"CPU cores: {multiprocessing.cpu_count()}")
        
        # Determine optimal number of workers for CPU
        num_workers = args.cpu_threads
        if num_workers <= 0:
            # Auto-detect: Use N-1 cores on systems with more than 2 cores
            num_workers = max(1, multiprocessing.cpu_count() - 1)
            logger.info(f"Auto-detected {num_workers} worker threads for CPU processing")
        
        transcriber = WhisperRealtime(
            model_size=args.model,
            language=args.language,
            use_gpu=not args.no_gpu,
            auto_detect=args.auto_detect,
            num_workers=num_workers
        )

        transcriber.start()
        
        # Main loop with graceful exit
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nStopping transcription...")
        finally:
            transcriber.stop()
            
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main() 