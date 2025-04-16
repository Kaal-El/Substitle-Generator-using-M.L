# Subtitle Generator using Machine Learning
This project uses machine learning to automatically generate subtitles from video or audio files. It leverages powerful speech recognition models to transcribe spoken content into time-aligned text, suitable for subtitles in `.srt` or `.txt` format.

## 🚀 Features
- Converts audio/video speech to text
- Outputs time-coded subtitles
- Supports various formats (.mp3, .wav, .mp4)
- Real-time and batch processing support
- Lightweight and extendable

## 🧠 Technologies Used
- **Python**
- **DeepSpeech / Whisper / SpeechRecognition** (ASR models)
- **Natural Language Processing (NLP)**
- **FFmpeg** for audio/video processing
- **Streamlit** (optional UI)
- **OpenCV** (if video frame analysis is required)
## ⚙️ Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Kaal-El/Substitle-Generator-using-M.L](https://github.com/Kaal-El/Substitle-Generator-using-M.L)
    cd Substitle-Generator-using-M.L
    ```

2.  **Navigate to the Subtitle-Generator directory:**
    ```bash
    cd Subtitle-Generator
    ```

3.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate   # On Windows
    ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **(Optional) Install FFmpeg:**
    * **Linux (Debian/Ubuntu):**
        ```bash
        sudo apt update
        sudo apt install ffmpeg
        ```
    * **macOS:**
        ```bash
        brew install ffmpeg
        ```
    * **Windows:** You can download the FFmpeg binaries from the official website and add them to your system's PATH.

6.  **(Optional) Install OpenCV:**
    ```bash
    pip install opencv-python
    ```
