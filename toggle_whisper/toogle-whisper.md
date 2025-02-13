# Configuration and Usage Instructions for toggle_whisper.sh

## Prerequisites

1. Install required tools:

~~~bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install ffmpeg
brew install ffmpeg

# Install OpenAI Whisper
pip install openai-whisper

# Verify everything works
ffmpeg --version
whisper --help
~~~

## Script Configuration

1. Create script file:

~~~bash
touch toggle_whisper.sh
chmod +x toggle_whisper.sh
~~~

2. Copy script content to toggle_whisper.sh file

## macOS Integration

1. Open Automator application

2. Create new Quick Action:
   - Choose: File → New → Quick Action
   - In "Workflow receives": select "no input"
   - In "Application": select "any application"

3. Add "Run Shell Script" action:
   - Drag "Run Shell Script" action from library
   - In script field enter full path to script:

4. Save Quick Action with a name (e.g., "Toggle Whisper")

5. Assign keyboard shortcut:
   - Open System Preferences
   - Go to Keyboard → Shortcuts
   - Select "Services"
   - Find created "Toggle Whisper" action
   - Double click next to name and set desired shortcut (e.g., ⌘⇧W)

## Usage

1. Start recording:
   - Press set keyboard shortcut
   - You'll see notification "Starting recording..."
   - System will start recording audio from default microphone

2. Stop recording and transcription:
   - Press same keyboard shortcut again
   - System will stop recording
   - Automatic transcription will begin
   - After completion, text will be automatically copied to clipboard
   - You'll receive completion notification

## Troubleshooting

1. If script reports missing tools:
   - Check if all required tools are installed
   - Make sure they are available in system path

2. Microphone issues:
   - Check system permissions for microphone
   - Make sure correct microphone is selected in system settings

3. Transcription problems:
   - Check internet connection
   - Ensure audio file was saved correctly
   - Check whisper logs in case of errors

## Notes

- Script creates temporary files in /tmp/ directory
- Files are automatically cleaned after transcription
- Default model is "small" and language is Polish
- You can adjust whisper parameters in script as needed
