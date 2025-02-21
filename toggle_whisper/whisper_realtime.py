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
from typing import Optional, List
from dataclasses import dataclass
from faster_whisper import WhisperModel
# Configure logging
# DEBUG for detailed output
# INFO for normal output
# ERROR for critical errors
# WARNING for warnings only
# CRITICAL for critical errors only

logging.basicConfig(level=logging.CRITICAL,
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
                 use_gpu: bool = True, auto_detect: bool = True):
        self.config = AudioConfig()
        self.audio_queue = queue.Queue()
        self.running = False
        self.silence_detector = SilenceDetector(
            threshold=self.config.SILENCE_THRESHOLD
        )
        self.clipboard = ClipboardManager()
        self.auto_detect = auto_detect
        
        # Initialize Whisper model with float32
        compute_type = "float32"  # Changed from float16 to float32
        device = "cuda" if use_gpu and torch.cuda.is_available() else "cpu"
        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type,
            download_root="/tmp/whisper_model"
        )
        
        # Audio interface
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.language = language
        
        # Print initial status for Raycast
        print("🎤 Whisper is ready!")
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
                        segments, _ = self.model.transcribe(
                            buffer,
                            language=None if self.auto_detect else self.language,
                            beam_size=5,
                            vad_filter=True,
                            vad_parameters=dict(
                                min_silence_duration_ms=500,
                                speech_pad_ms=400
                            )
                        )
                        
                        text = " ".join(segment.text for segment in segments)
                        if text.strip():
                            self.clipboard.update(text)
                            # Display transcription clearly
                            print("\n" + "="*50)
                            print(f"📝 Transcription: {text}")
                            print("="*50 + "\n")
                            sys.stdout.flush()
                    
                    # Reset buffer but keep a small overlap
                    buffer = buffer[-int(self.config.RATE * 0.5):] if len(buffer) > 0 else buffer
                    silence_counter = 0
                
            except queue.Empty:
                continue
            except Exception as e:
                print(f"❌ Error: {str(e)}", file=sys.stderr)
                sys.stderr.flush()

    def start(self):
        """Start the transcription system"""
        self.running = True
        
        # Start audio stream
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
        self.process_thread.start()
        
        print("Whisper is listening...", flush=True)
        sys.stdout.flush()

    def stop(self):
        """Stop the transcription system"""
        self.running = False
        if self.process_thread:
            self.process_thread.join()
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
    parser.add_argument("--model", default="small", help="Whisper model size")
    parser.add_argument("--language", default="en", help="Language code (ignored if --auto-detect is used)")
    parser.add_argument("--no-gpu", action="store_true", help="Disable GPU acceleration")
    parser.add_argument("--auto-detect", action="store_true", help="Enable automatic language detection")
    args = parser.parse_args()

    try:
        logger.info("Starting whisper_realtime.py")
        logger.info(f"Python version: {sys.version}")
        logger.info(f"PyAudio version: {pyaudio.__version__}")
        logger.info(f"Torch version: {torch.__version__}")
        logger.info(f"CUDA available: {torch.cuda.is_available()}")
        
        # Initialize audio
        logger.info("Initializing PyAudio...")
        audio = pyaudio.PyAudio()
        
        transcriber = WhisperRealtime(
            model_size=args.model,
            language=args.language,
            use_gpu=not args.no_gpu,
            auto_detect=args.auto_detect
        )

        transcriber.start()
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        transcriber.stop()
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main() 