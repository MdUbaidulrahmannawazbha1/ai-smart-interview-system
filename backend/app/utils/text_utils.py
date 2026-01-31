"""
Text processing utilities
"""
import re
from typing import List, Set


def clean_text(text: str) -> str:
    """
    Clean and normalize text
    
    Args:
        text: Input text
        
    Returns:
        Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters except basic punctuation
    text = re.sub(r'[^a-zA-Z0-9\s\.,!?-]', '', text)
    # Strip leading/trailing whitespace
    text = text.strip()
    return text


def extract_keywords(text: str) -> Set[str]:
    """
    Extract keywords from text
    
    Args:
        text: Input text
        
    Returns:
        Set of keywords
    """
    # Convert to lowercase and split
    words = text.lower().split()
    
    # Common stop words to filter out
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
        'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
        'who', 'when', 'where', 'why', 'how'
    }
    
    # Filter stop words and short words
    keywords = {word for word in words if word not in stop_words and len(word) > 2}
    
    return keywords


def calculate_keyword_match_score(text: str, expected_keywords: List[str]) -> float:
    """
    Calculate keyword match score
    
    Args:
        text: Input text
        expected_keywords: List of expected keywords
        
    Returns:
        Match score (0 to 1)
    """
    if not expected_keywords:
        return 0.5  # Neutral score if no keywords provided
    
    text_keywords = extract_keywords(text)
    expected_set = {kw.lower() for kw in expected_keywords}
    
    # Calculate how many expected keywords are present
    matches = len(text_keywords.intersection(expected_set))
    score = matches / len(expected_set) if expected_set else 0.0
    
    return min(score, 1.0)


def truncate_text(text: str, max_length: int = 500) -> str:
    """
    Truncate text to maximum length
    
    Args:
        text: Input text
        max_length: Maximum length
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    
    # Try to truncate at sentence boundary
    truncated = text[:max_length]
    last_period = truncated.rfind('.')
    
    if last_period > max_length * 0.7:  # If we can find a reasonable sentence boundary
        return truncated[:last_period + 1]
    
    return truncated + "..."
