"""
Video Processing Module
Optional: Can be used for extracting video frames for synchronization or visuals.
"""

import cv2

def extract_frames(video_path, output_folder="frames", frame_rate=1):
    """
    Extracts frames from the video at a specified frame rate.
    """
    vidcap = cv2.VideoCapture(video_path)
    count = 0
    success, image = vidcap.read()
    while success:
        if count % frame_rate == 0:
            filename = f"{output_folder}/frame{count}.jpg"
            cv2.imwrite(filename, image)
        success, image = vidcap.read()
        count += 1
