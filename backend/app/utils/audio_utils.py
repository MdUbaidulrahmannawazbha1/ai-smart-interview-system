"""
audio_utils.py

Audio processing utility module for AI-Powered Smart Interview System.
Provides functions for audio file validation and processing.
"""

from typing import Optional, Tuple
import os


SUPPORTED_AUDIO_FORMATS = ['.mp3', '.wav', '.ogg', '.flac', '.m4a', '.webm']
MAX_AUDIO_SIZE_MB = 25


def validate_audio_file(file_path: str) -> Tuple[bool, Optional[str]]:
    """
    Validate an audio file for processing.
    
    Args:
        file_path: Path to the audio file
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check if file exists
    if not os.path.exists(file_path):
        return False, "Audio file does not exist"
    
    # Check file extension
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in SUPPORTED_AUDIO_FORMATS:
        return False, f"Unsupported audio format. Supported formats: {', '.join(SUPPORTED_AUDIO_FORMATS)}"
    
    # Check file size
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if file_size_mb > MAX_AUDIO_SIZE_MB:
        return False, f"Audio file too large. Maximum size: {MAX_AUDIO_SIZE_MB}MB"
    
    return True, None


def get_audio_format(file_path: str) -> Optional[str]:
    """
    Get the audio format/extension from a file path.
    
    Args:
        file_path: Path to the audio file
        
    Returns:
        str: Audio format (e.g., 'mp3', 'wav') or None if invalid
    """
    if not file_path:
        return None
    
    _, ext = os.path.splitext(file_path)
    return ext.lower().lstrip('.')


def is_audio_file(file_path: str) -> bool:
    """
    Check if a file is a supported audio file.
    
    Args:
        file_path: Path to check
        
    Returns:
        bool: True if file is a supported audio format
    """
    _, ext = os.path.splitext(file_path)
    return ext.lower() in SUPPORTED_AUDIO_FORMATS


def format_audio_duration(seconds: float) -> str:
    """
    Format audio duration in seconds to a human-readable string.
    
    Args:
        seconds: Duration in seconds
        
    Returns:
        str: Formatted duration (e.g., "2:35" for 2 minutes 35 seconds)
    """
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes}:{secs:02d}"
