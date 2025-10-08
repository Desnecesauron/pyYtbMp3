# Gemini Code Assistant Context

## Project Overview

This project, `pyYtbMp3`, is a Python-based graphical utility for downloading video and audio from various online platforms, including YouTube, Facebook, Twitter, GloboPlay, and Instagram. It allows users to paste a URL and choose to download the content as either an MP4 video or an MP3 audio file.

The application is built using:

*   **Python:** The core programming language.
*   **Tkinter:** For the graphical user interface (GUI), providing a simple window with a URL input field, download buttons, and a status log.
*   **youtube-dl:** A powerful library for extracting video information and handling the download process from a wide range of websites.
*   **Threading:** The application uses Python's `threading` module to run download operations in separate threads, preventing the GUI from freezing during the download process.

The main application logic is contained entirely within the `main.py` file. An executable version, `main.exe`, is also present, suggesting it has been packaged for Windows users.

## Building and Running

This project is a Python script with a GUI and does not have a formal build process or command-line interface defined in the source code.

### Prerequisites

To run this project from the source, you will need:

1.  **Python 3.x**
2.  The **`youtube-dl`** library. It can be installed via pip:
    ```bash
    pip install youtube-dl
    ```
3.  The **`ffmpeg`** tool. `youtube-dl` requires `ffmpeg` to be installed and available in the system's PATH for converting and processing video/audio files, especially for creating MP3s.

### Running the Application

To run the application from the source code, execute the `main.py` script:

```bash
python main.py
```

This will launch the Tkinter GUI window.

### Running the Executable

The `main.exe` file is a pre-packaged executable for Windows. It can be run by double-clicking the file or executing it from a Windows command prompt.

```bash
./main.exe
```

## Development Conventions

Based on the existing code in `main.py`, the following conventions can be observed:

*   **Structure:** The entire application, including the GUI, download logic, and threading, is contained within a single file (`main.py`).
*   **GUI:** The GUI is implemented using Python's standard `tkinter` library.
*   **Concurrency:** Downloads are handled in separate threads (`runMP3`, `runMP4`) to keep the UI responsive.
*   **Error Handling:** The code includes `try...except` blocks to catch potential errors during the download process (e.g., invalid URLs, network issues) and displays error messages in the GUI's logbox.
*   **File Naming:** Downloaded files are named based on the video title. For Facebook videos, a random number is used to generate a unique filename.
