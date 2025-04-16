"""
Utility functions for subtitle formatting, saving, etc.
"""

def save_subtitles(subtitles, output_path, format='srt'):
    """
    Save subtitles to file in specified format (srt or txt).
    """
    with open(output_path, "w", encoding="utf-8") as f:
        if format == "srt":
            for idx, (start, end, text) in enumerate(subtitles):
                f.write(f"{idx+1}\n{start} --> {end}\n{text}\n\n")
        else:
            for _, _, text in subtitles:
                f.write(f"{text}\n")
