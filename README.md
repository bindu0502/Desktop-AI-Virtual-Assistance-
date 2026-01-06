# AI Virtual Assistant

A simple AI-powered virtual assistant built with Python, featuring a graphical user interface (GUI), speech recognition, and text-to-speech capabilities.

## Features

- **Voice Commands**: Interact using speech recognition (requires microphone and internet).
- **Text-to-Speech**: Responses are spoken aloud using pyttsx3.
- **GUI Interface**: Tkinter-based window for text input/output and buttons.
- **Commands Supported**:
  - Greetings: "hello", "good morning", "how are you"
  - Time: "time now"
  - Weather: "weather" (requires API key in weather.py)
  - Web Browsing: "open google", "youtube"
  - Music: "play music" (opens Gaana), "music from my laptop" (plays from D:\music)
  - Shutdown: "shutdown" or "quit"

## Requirements

- Python 3.8+
- Windows (for pyttsx3 TTS and microphone access)
- Internet connection (for Google speech recognition)
- Microphone enabled

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/bindu0502/Desktop-AI-Virtual-Assistance-.git
   cd Desktop-AI-Virtual-Assistance-
   ```

2. Create a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```
   pip install pyttsx3 SpeechRecognition requests_html Pillow pyaudio lxml_html_clean
   ```

## Usage

Run the GUI application:
```
python vir/GUI.py
```

- Use the "ASK" button for voice input.
- Type in the text box and press "Send" for text input.
- Press "Delete" to clear the chat.

## Project Structure

- `vir/GUI.py`: Main GUI application.
- `vir/action.py`: Command processing logic.
- `vir/speak.py`: Text-to-speech functionality.
- `vir/spech_to_text.py`: Speech-to-text functionality.
- `vir/weather.py`: Weather information (incomplete).
- `image/`: GUI images.

## Notes

- Speech recognition uses Google's API, so internet is required.
- Weather feature needs a valid API key in `weather.py`.
- Music from laptop assumes songs in `D:\music`.
- The assistant may not handle all variations of commands perfectly.

## Contributing

Feel free to fork and contribute improvements!

## License

This project is open-source. Use at your own risk.