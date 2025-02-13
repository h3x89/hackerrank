#!/bin/bash

# toggle_whisper.sh
# Script for toggling audio recording and transcription using OpenAI Whisper
# Requirements:
#   - ffmpeg (audio recording)
#   - whisper (OpenAI transcription)
#   - osascript (macOS notifications)
#   - pbcopy (clipboard copying)

# Temporary files and configuration
LOCKFILE="/tmp/whisper_recording.pid"
AUDIOFILE="/tmp/whisper_input.wav"
TRANSCRIPT="/tmp/whisper_output.txt"

# Function for displaying messages and notifications
show_notification() {
    local message="$1"
    echo "[Whisper Toggle] $message"
    osascript -e "display notification \"$message\" with title \"Whisper Toggle\""
}

# Function for cleaning temporary files
cleanup() {
    [ -f "$AUDIOFILE" ] && rm "$AUDIOFILE"
    [ -f "$TRANSCRIPT" ] && rm "$TRANSCRIPT"
    [ -f "${AUDIOFILE%.*}.txt" ] && rm "${AUDIOFILE%.*}.txt"
}

# Function for displaying file size
show_file_info() {
    local file="$1"
    local size=$(ls -lh "$file" | awk '{print $5}')
    local duration=$(ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$file" 2>/dev/null)
    duration=$(printf "%.1f" "$duration")
    show_notification "File size: $size, Recording length: ${duration}s"
}

# Function for displaying progress bar
show_progress() {
    local message="$1"
    echo -ne "\r[Whisper Toggle] $message"
}

# Function for checking and installing requirements
check_requirements() {
    for cmd in ffmpeg whisper osascript pbcopy; do
        if ! command -v $cmd >/dev/null 2>&1; then
            show_notification "Installing missing tool: $cmd"
            case $cmd in
                ffmpeg)
                    brew install ffmpeg
                    ;;
                whisper)
                    pip3 install -U openai-whisper
                    ;;
                osascript|pbcopy)
                    show_notification "Error: Missing system tool: $cmd"
                    exit 1
                    ;;
            esac
        fi
    done
}

# Check requirements
check_requirements

# Main script logic
if [ ! -f "$LOCKFILE" ]; then
    # Start recording
    show_notification "Starting recording..."
    
    # Start recording in background with better quality
    ffmpeg -f avfoundation -i ":0" -ar 16000 -ac 1 "$AUDIOFILE" -y >/dev/null 2>&1 &
    
    # Save recording process PID
    echo $! > "$LOCKFILE"
    show_notification "Recording started. Run script again to stop."
else
    # Stop recording
    show_notification "Stopping recording..."
    
    # Get and terminate recording process
    PID=$(cat "$LOCKFILE")
    kill "$PID" 2>/dev/null
    rm "$LOCKFILE"
    
    # Wait for ffmpeg to close file and show progress
    for i in {1..3}; do
        show_progress "Finalizing recording... ($i/3)"
        sleep 1
    done
    echo # New line after progress bar
    
    if [ ! -f "$AUDIOFILE" ]; then
        show_notification "Error: Audio file not found!"
        cleanup
        exit 1
    fi
    
    # Show recorded file information
    show_file_info "$AUDIOFILE"
    
    # Start transcription
    show_notification "Starting transcription..."
    
    # Call Whisper with specified parameters and progress display
    echo "[Whisper Toggle] Processing transcription..."
    
    # Save whisper output to temporary file for debugging
    WHISPER_LOG="/tmp/whisper_log.txt"
    
    # Change to temporary directory before running whisper
    cd /tmp
    
    # Use whisper with additional parameters for better quality
    if ! whisper "$AUDIOFILE" \
        --model small \
        --language pl \
        --output_format txt \
        --device cpu \
        --temperature 0.0 \
        --condition_on_previous_text False \
        --output_dir /tmp \
        2>&1 | tee "$WHISPER_LOG"; then
        
        show_notification "Error: Problem occurred during transcription!"
        echo "Whisper log:"
        cat "$WHISPER_LOG"
        cleanup
        exit 1
    fi
    
    # Display progress from log
    while IFS= read -r line; do
        if [[ $line == *"Detected language:"* ]] || 
           [[ $line == *"Transcribing"* ]] || 
           [[ $line == *"Loading"* ]]; then
            show_notification "$line"
        fi
    done < "$WHISPER_LOG"
    
    # Remove log file
    rm -f "$WHISPER_LOG"

    # Check transcription result (now looking in /tmp)
    WHISPER_OUTPUT="/tmp/whisper_input.txt"
    if [ ! -f "$WHISPER_OUTPUT" ]; then
        show_notification "Error: Transcription failed!"
        echo "Missing output file: $WHISPER_OUTPUT"
        # Show directory contents for debugging
        echo "Contents of /tmp:"
        ls -l /tmp/whisper*
        cleanup
        exit 1
    fi
    
    # Move result to destination file
    mv "$WHISPER_OUTPUT" "$TRANSCRIPT"
    
    # Show transcription contents for debugging
    echo "Transcription contents:"
    cat "$TRANSCRIPT"
    
    # Copy transcription to clipboard
    if cat "$TRANSCRIPT" | pbcopy; then
        show_notification "Transcription complete. Text has been copied to clipboard."
    else
        show_notification "Error: Failed to copy text to clipboard!"
    fi
    
    # Cleanup
    cleanup
fi