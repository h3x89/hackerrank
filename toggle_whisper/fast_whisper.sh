#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Fast Whisper Transcription
# @raycast.mode fullOutput


# Optional parameters:
# @raycast.icon ⚡
# @raycast.packageName Whisper
# @raycast.argument1 { "type": "text", "placeholder": "Model Size", "optional": true }
# @raycast.argument2 { "type": "text", "placeholder": "Language", "optional": true }
# @raycast.argument3 { "type": "text", "placeholder": "Debug Mode", "optional": true }
# @raycast.argument4 { "type": "text", "placeholder": "Batch Size", "optional": true }
# @raycast.argument5 { "type": "text", "placeholder": "Use Original", "optional": true }

# Documentation:
# @raycast.description Fast Whisper implementation, optimized for English
# @raycast.author robert_kubis
# @raycast.authorURL https://github.com/h3x89

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Script directory: $SCRIPT_DIR"

# Set PYTHONPATH to ensure consistent environment
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"

# Check if running on Apple Silicon
if [[ $(uname -m) == 'arm64' ]]; then
    IS_APPLE_SILICON=true
    echo "🍎 Detected Apple Silicon (M1/M2)"
else
    IS_APPLE_SILICON=false
fi

# Function to run the original Whisper implementation
run_original_whisper() {
    echo "🔄 Switching to original Whisper implementation..."
    
    # Calculate CPU workers based on system
    if [ "$IS_APPLE_SILICON" = true ]; then
        CPU_WORKERS=4
    else
        CPU_WORKERS=$(( $(sysctl -n hw.ncpu) / 2 ))
    fi
    
    # Set debug flag
    if [ "$DEBUG_MODE" = "true" ]; then
        DEBUG_FLAG="--debug"
    else
        DEBUG_FLAG=""
    fi
    
    # Set language flag
    if [ -z "$LANGUAGE" ]; then
        LANG_FLAG="--auto-detect"
    else
        LANG_FLAG="--language $LANGUAGE"
    fi
    
    echo "Starting original Whisper with model: $MODEL_SIZE, language: $LANGUAGE, CPU workers: $CPU_WORKERS"
    python3 "$SCRIPT_DIR/standard_whisper.py" --model "$MODEL_SIZE" $LANG_FLAG $DEBUG_FLAG --cpu_threads $CPU_WORKERS
}

# Activate virtual environment if it exists
if [ -d "$SCRIPT_DIR/venv" ]; then
    source "$SCRIPT_DIR/venv/bin/activate"
    echo "Activated virtual environment."
else
    echo "Virtual environment not found, using system Python."
fi

# Set default values
MODEL_SIZE=${1:-small}
LANGUAGE=${2:-}
DEBUG_MODE=${3:-false}
BATCH_SIZE=${4:-2}
USE_ORIGINAL=${5:-false}

echo "Model size: $MODEL_SIZE"
echo "Language: $LANGUAGE (empty=auto-detect)"
echo "Debug mode: $DEBUG_MODE"
echo "Batch size: $BATCH_SIZE"
echo "Use original: $USE_ORIGINAL"

# Check if we should use the original implementation
if [ "$USE_ORIGINAL" = "true" ]; then
    run_original_whisper
    exit 0
fi

# Check if language is Polish - use original implementation for better results
if [ "$LANGUAGE" = "pl" ]; then
    echo "🇵🇱 Polish language detected. Using original Whisper for better results."
    run_original_whisper
    exit 0
fi

# Validate model size
if [[ ! "$MODEL_SIZE" =~ ^(tiny|base|small|medium|large)$ ]]; then
    echo "⚠️ Invalid model size: $MODEL_SIZE. Using 'small' instead."
    MODEL_SIZE="small"
fi

# Check if insanely-fast-whisper is installed
if ! python3 -c "import importlib.util; print(importlib.util.find_spec('insanely_fast_whisper') is not None)" | grep -q "True"; then
    echo "⚠️ insanely-fast-whisper is not installed. Falling back to original Whisper."
    run_original_whisper
    exit 0
fi

# Check if insanely-fast-whisper command works
if ! python3 -c "import subprocess; subprocess.run(['insanely-fast-whisper', '--help'], capture_output=True, text=True)" > /dev/null 2>&1; then
    echo "⚠️ insanely-fast-whisper command not working. Falling back to original Whisper."
    run_original_whisper
    exit 0
fi

# Set debug flag
if [ "$DEBUG_MODE" = "true" ]; then
    DEBUG_FLAG="--debug"
else
    DEBUG_FLAG=""
fi

# Run the Python script
echo "Starting Fast Whisper transcription with model: $MODEL_SIZE, batch size: $BATCH_SIZE"
python3 "$SCRIPT_DIR/fast_whisper.py" --model "$MODEL_SIZE" --batch-size "$BATCH_SIZE" $DEBUG_FLAG ${LANGUAGE:+--language "$LANGUAGE"}

# Deactivate virtual environment
if [ -d "$SCRIPT_DIR/venv" ]; then
    deactivate
fi

exit 0 