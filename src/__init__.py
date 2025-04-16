# Initialize the subtitle generator module
from .audio_processing import extract_audio
from .video_processing import extract_frames
from .subtitle_generator import generate_subtitles
from .utils import save_subtitles
"""
Subtitle Generator Package
Author: Rishabh Singh
Description: Converts audio/video to time-coded subtitles using ML.
"""
__version__ = "1.0.0"
