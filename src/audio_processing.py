"""
Audio Processing Module
Handles loading and preprocessing of audio files.
"""

import ffmpeg
import os

def extract_audio(input_file, output_audio="temp.wav"):
    """
    Extract audio from video file using ffmpeg.
    """
    try:
        ffmpeg.input(input_file).output(output_audio, ac=1, ar='16000').run(overwrite_output=True)
        return output_audio
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None
