"""
text_utils.py

Text processing utility module for AI-Powered Smart Interview System.
Provides text cleaning, normalization, and preprocessing functions.
"""

import re
from typing import List


def clean_text(text: str) -> str:
    """
    Clean and normalize text by removing extra whitespace and special characters.
    
    Args:
        text: Input text to clean
        
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def remove_special_characters(text: str, keep_spaces: bool = True) -> str:
    """
    Remove special characters from text, optionally keeping spaces.
    
    Args:
        text: Input text
        keep_spaces: Whether to keep spaces in the text
        
    Returns:
        str: Text with special characters removed
    """
    if not text:
        return ""
    
    if keep_spaces:
        # Keep alphanumeric characters and spaces
        pattern = r'[^a-zA-Z0-9\s]'
    else:
        # Keep only alphanumeric characters
        pattern = r'[^a-zA-Z0-9]'
    
    cleaned = re.sub(pattern, '', text)
    return cleaned


def truncate_text(text: str, max_length: int = 500, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length, adding suffix if truncated.
    
    Args:
        text: Input text
        max_length: Maximum length of output text
        suffix: Suffix to add if text is truncated
        
    Returns:
        str: Truncated text
    """
    if not text or len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def tokenize_text(text: str) -> List[str]:
    """
    Simple tokenization of text into words.
    
    Args:
        text: Input text
        
    Returns:
        list: List of tokens/words
    """
    if not text:
        return []
    
    # Clean and split by whitespace
    cleaned = clean_text(text)
    tokens = cleaned.split()
    
    return tokens


def normalize_whitespace(text: str) -> str:
    """
    Normalize whitespace in text to single spaces.
    
    Args:
        text: Input text
        
    Returns:
        str: Text with normalized whitespace
    """
    if not text:
        return ""
    
    # Replace all whitespace sequences with single space
    normalized = ' '.join(text.split())
    
    return normalized
