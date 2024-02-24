# PDF to Audio Converter

This Python script utilizes the `gtts` library for text-to-speech conversion and `PyPDF2` for reading PDF files. The script reads the content from a PDF file and converts it into an audio file in MP3 format.

## Features

- **PDF Reading:** Utilizes PyPDF2 to extract text content from a PDF file.

- **Text-to-Speech Conversion:** Utilizes gTTS (Google Text-to-Speech) for converting the extracted text into an audio file.

## Tech Stack

- **gtts:** Python library for Google Text-to-Speech.

- **PyPDF2:** Python library for reading PDF files.

## Usage

1. **Run the Script:**
   - Execute the script using Python: `python pdf_to_audio_converter.py`.

2. **Check Output:**
   - Find the generated audio file named "Audio.mp3" in the same directory.

## Code Snippet

```python
from gtts import gTTS
import PyPDF2
```

## Notes
- Ensure you have the necessary dependencies installed before running the script.

## License
- This script is licensed under the MIT License - see the LICENSE file for details.
