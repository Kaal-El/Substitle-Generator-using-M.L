"""
Main Subtitle Generator
Uses speech recognition to convert audio to subtitles with timestamps.
"""

import os
import whisper
from src.audio_processing import extract_audio
from src.utils import save_subtitles

def transcribe_audio(audio_path, model_name="base"):
    """
    Transcribe audio using Whisper.
    """
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result

def format_segments(segments):
    """
    Format segments into (start, end, text) tuples.
    """
    formatted = []
    for seg in segments:
        formatted.append((format_timestamp(seg['start']), format_timestamp(seg['end']), seg['text'].strip()))
    return formatted

def format_timestamp(seconds):
    """
    Convert seconds to SRT timestamp format.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def generate_subtitles(input_file, output_format="srt"):
    """
    Main function to generate subtitles from audio/video.
    """
    audio_file = extract_audio(input_file)
    result = transcribe_audio(audio_file)
    segments = format_segments(result["segments"])
    output_path = os.path.join("outputs", os.path.splitext(os.path.basename(input_file))[0] + f".{output_format}")
    save_subtitles(segments, output_path, output_format)
    print(f"Subtitles saved to {output_path}")
