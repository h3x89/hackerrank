#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Standard Whisper Transcription
# @raycast.mode fullOutput


# Optional parameters:
# @raycast.icon 🎙️
# @raycast.packageName Whisper
# @raycast.argument1 { "type": "text", "placeholder": "Model Size", "optional": true }
# @raycast.argument2 { "type": "text", "placeholder": "Debug Mode", "optional": true }
# @raycast.argument3 { "type": "text", "placeholder": "CPU Threads", "optional": true }

# Documentation:
# @raycast.description Original Whisper implementation, best for Polish transcription
# @raycast.author robert_kubis
# @raycast.authorURL https://github.com/h3x89

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Script directory: $SCRIPT_DIR"

# Check if running on Apple Silicon
if [[ $(uname -m) == 'arm64' ]]; then
    IS_APPLE_SILICON=true
    echo "🍎 Detected Apple Silicon (M1/M2)"
else
    IS_APPLE_SILICON=false
fi

# Activate virtual environment if it exists
if [ -d "$SCRIPT_DIR/venv" ]; then
    echo "Activating virtual environment..."
    source "$SCRIPT_DIR/venv/bin/activate"
else
    echo "Virtual environment not found, using system Python."
fi

# Set default values
MODEL_SIZE=${1:-small}
echo "Using model size: $MODEL_SIZE"

# Debug mode
DEBUG_MODE=${2:-false}
DEBUG_FLAG=""
if [[ "$DEBUG_MODE" == "true" ]]; then
    echo "Debug mode enabled"
    DEBUG_FLAG="--debug"
fi

# CPU threads
CPU_THREADS=${3:-0}
echo "CPU threads: $CPU_THREADS (0=auto)"

# Calculate CPU workers based on system
if [ "$CPU_THREADS" = "0" ]; then
    if [ "$IS_APPLE_SILICON" = true ]; then
        CPU_WORKERS=4
    else
        CPU_WORKERS=$(( $(sysctl -n hw.ncpu) / 2 ))
    fi
else
    CPU_WORKERS=$CPU_THREADS
fi

# Validate model size
case $MODEL_SIZE in
    tiny|base|small|medium)
        ;;
    *)
        echo "Invalid model size. Using default: small"
        MODEL_SIZE="small"
        ;;
esac

# Run the Python script
echo "Starting transcription with model: $MODEL_SIZE, CPU workers: $CPU_WORKERS"
python3 "$SCRIPT_DIR/standard_whisper.py" --model $MODEL_SIZE $DEBUG_FLAG --cpu_threads $CPU_WORKERS

# Deactivate virtual environment
if [ -d "$SCRIPT_DIR/venv" ]; then
    echo "Deactivating virtual environment..."
    deactivate
fi