#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Whisper Transcription sh
# @raycast.mode fullOutput


# Optional parameters:
# @raycast.icon 🎤
# @raycast.packageName Whisper
# @raycast.argument1 { "type": "text", "placeholder": "Model Size (tiny/base/small/medium)", "optional": true }

# Documentation:
# @raycast.description Real-time audio transcription using Whisper
# @raycast.author robert_kubis
# @raycast.authorURL https://github.com/h3x89

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Script directory: $SCRIPT_DIR"

# Activate virtual environment
echo "Activating virtual environment..."
source "${SCRIPT_DIR}/venv/bin/activate"

# Default model size if not specified
MODEL_SIZE=${1:-"small"}
echo "Using model size: $MODEL_SIZE"

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
echo "Running Python script..."
python3 "${SCRIPT_DIR}/whisper_realtime.py" --model "$MODEL_SIZE" --auto-detect

# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate