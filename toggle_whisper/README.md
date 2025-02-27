# Whisper Transcription Tools

A collection of real-time speech-to-text transcription tools using Whisper models. Optimized for macOS with Apple Silicon (M1/M2) chips.

## Project Overview

This project offers several implementations of OpenAI's Whisper speech recognition system, each optimized for different use cases. The tools have evolved from basic two-step recording and transcription processes to sophisticated real-time speech recognition solutions with specialized optimizations.

### Evolution of the Tools

1. **Legacy Scripts** - Basic implementation with separate recording and transcription steps
2. **Standard Scripts** - Balanced implementation with real-time capabilities
3. **Specialized Scripts** - Optimized implementations for specific languages and performance needs

## Available Scripts

### Modern Implementations

#### 1. Standard Whisper Transcription (`standard_whisper.sh` & `standard_whisper.py`)

A balanced implementation using the `faster_whisper` library, offering a good compromise between speed and accuracy for most languages.

```bash
./standard_whisper.sh [model] [debug] [cpu_threads]
```

**Key Features**:

- Universal solution suitable for most languages
- Uses `faster_whisper` for improved performance over the original Whisper
- Adaptive silence detection for better speech recognition
- Supports automatic language detection
- Multi-core CPU optimization

**Parameters**:

- `model` - Whisper model size (tiny, base, small, medium) - default: small
- `debug` - Debug mode (true/false) - default: false
- `cpu_threads` - Number of CPU threads (0=auto) - default: auto

**Example**:

```bash
./standard_whisper.sh small false 4
```

**When to use**: When you need a reliable all-around solution for transcription in various languages.

#### 2. Fast Whisper Transcription (`fast_whisper.sh` & `fast_whisper.py`)

The fastest transcription implementation using the "Insanely Fast Whisper" library. Optimized for maximum performance, particularly with English language content.

```bash
./fast_whisper.sh [model] [language] [debug] [batch_size] [use_original]
```

**Key Features**:

- Uses the "Insanely Fast Whisper" library - 5-8x faster than standard Whisper
- Real-time transcription with minimal latency
- Batch processing for performance optimization
- Flash attention mechanism for better efficiency
- Automatic fallback to standard implementation for non-English languages

**Parameters**:

- `model` - Model size (tiny, base, small, medium) - default: small
- `language` - Language code (en/pl/fr/etc., empty=auto) - default: auto
- `debug` - Debug mode (true/false) - default: false
- `batch_size` - Batch size (1-8) - default: 2
- `use_original` - Force using original implementation (true/false) - default: false

**Example**:

```bash
./fast_whisper.sh small en false 4 false
```

**When to use**: When speed is a priority and you're primarily working with English content.

#### 3. Polish Whisper Transcription (`polish_whisper.sh` & `polish_whisper.py`)

A specialized implementation optimized specifically for Polish language transcription, offering the best quality for Polish speech recognition.

```bash
./polish_whisper.sh [model] [language] [debug]
```

**Key Features**:

- Specially tuned parameters for Polish language
- Increased beam size (5) for better Polish word recognition
- Customized Voice Activity Detection for Polish speech patterns
- Default language set to Polish
- Balanced for quality and speed in Polish transcription

**Parameters**:

- `model` - Model size (tiny, base, small, medium) - default: small
- `language` - Language code (en/pl/fr/etc., empty=auto) - default: pl
- `debug` - Debug mode (true/false) - default: false

**Example**:

```bash
./polish_whisper.sh small pl false
```

**When to use**: When you need the highest quality transcription for Polish language content.

### Legacy Implementations

#### 4. Toogle Whisper (`toogle-whisper.sh`)

The original implementation that uses a two-step process: first recording an audio file, then transcribing it.

**Key Features**:

- Two-stage process (record then transcribe)
- Slower due to the non-streaming approach
- No real-time feedback
- Basic implementation without optimizations

**When to use**: Generally not recommended unless you specifically need the two-step process for archiving both audio and transcription.

#### 5. Whisper Transcribe (`whisper-transcribe.sh` & `whisper_realtime.py`)

An improved version of the original implementation that introduced real-time capabilities but with limited optimizations.

**Key Features**:

- CPU-based processing
- Basic real-time capabilities
- Limited silence detection and buffering
- Less optimized than newer implementations

**When to use**: Generally superseded by the newer implementations, but useful as a reference implementation.

## Differences Between Modern Implementations

1. **Standard Whisper** (`standard_whisper.py`):
   - Uses the `faster_whisper` library
   - Good balance between speed and accuracy
   - Works well for most languages
   - CPU-optimized for Apple Silicon

2. **Fast Whisper** (`fast_whisper.py`):
   - Uses the `insanely-fast-whisper` library
   - Significantly faster transcription speed (5-8x)
   - Best for English language
   - May have reduced accuracy for non-English languages
   - Automatically falls back to standard implementation for Polish

3. **Polish Whisper** (`polish_whisper.py`):
   - Specifically tuned for Polish language
   - Enhanced parameters for better Polish recognition
   - Increased beam size for better word accuracy
   - Voice Activity Detection optimized for Polish speech patterns
   - Most reliable option for Polish transcription

## Technical Comparison

| Feature | Standard Whisper | Fast Whisper | Polish Whisper | Toogle Whisper | Whisper Transcribe |
|---------|-----------------|--------------|----------------|----------------|-------------------|
| Speed | Medium | Very Fast | Medium | Slow | Medium-Slow |
| English accuracy | High | High | High | Medium | Medium |
| Polish accuracy | Good | Poor | Excellent | Poor | Medium |
| Real-time | Yes | Yes | Yes | No | Yes |
| Silence detection | Advanced | Advanced | Advanced | None | Basic |
| Environment | CPU/GPU | CPU/GPU | CPU/GPU | CPU | CPU |
| Implementation | faster_whisper | insanely-fast-whisper | faster_whisper | basic | basic |

## Requirements

The scripts require a Python environment with the appropriate libraries:

```
pip install -r requirements.txt
```

Additionally, for the Fast Whisper script, the Insanely Fast Whisper library is needed:

```
pip install insanely-fast-whisper
```

## Raycast Integration

The scripts are optimized for use with the Raycast application. Simply add the script as a command in Raycast for quick access to transcription. The Polish Whisper script is particularly recommended for Raycast use with Polish language.

## Author

Robert Kubis (<https://github.com/h3x89>)
