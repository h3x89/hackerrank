#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Polish Whisper Transcription
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🇵🇱
# @raycast.packageName Whisper
# @raycast.argument1 { "type": "text", "placeholder": "Model Size", "optional": true }
# @raycast.argument2 { "type": "text", "placeholder": "Language", "optional": true }
# @raycast.argument3 { "type": "text", "placeholder": "Debug Mode", "optional": true }

# Documentation:
# @raycast.description Reliable audio transcription optimized for Polish language
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
LANGUAGE=${2:-pl}
DEBUG_MODE=${3:-false}

echo "Using model size: $MODEL_SIZE"
echo "Language: $LANGUAGE (empty=auto-detect)"
echo "Debug mode: $DEBUG_MODE"

# Set debug flag
if [ "$DEBUG_MODE" = "true" ]; then
    echo "Debug mode enabled"
    DEBUG_FLAG="--debug"
else
    DEBUG_FLAG=""
fi

# Set language flag
if [ -z "$LANGUAGE" ]; then
    LANG_FLAG="--auto-detect"
    echo "Using automatic language detection"
else
    LANG_FLAG="--language $LANGUAGE"
    echo "Setting language to: $LANGUAGE"
fi

# Calculate CPU workers based on system
if [ "$IS_APPLE_SILICON" = true ]; then
    CPU_WORKERS=4
else
    CPU_WORKERS=$(( $(sysctl -n hw.ncpu) / 2 ))
fi
echo "Using $CPU_WORKERS CPU workers"

# Validate model size
if [[ ! "$MODEL_SIZE" =~ ^(tiny|base|small|medium|large)$ ]]; then
    echo "⚠️ Invalid model size: $MODEL_SIZE. Using 'small' instead."
    MODEL_SIZE="small"
fi

# Run the Python script
echo "Starting Polish-optimized transcription with model: $MODEL_SIZE"
python3 "$SCRIPT_DIR/polish_whisper.py" --model "$MODEL_SIZE" $LANG_FLAG $DEBUG_FLAG --cpu_threads $CPU_WORKERS

# Deactivate virtual environment
if [ -d "$SCRIPT_DIR/venv" ]; then
    echo "Deactivating virtual environment..."
    deactivate
fi

exit 0 