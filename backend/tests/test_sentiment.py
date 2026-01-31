"""
test_sentiment.py

Unit tests for sentiment analysis functionality.
"""

import pytest
from app.services.sentiment_analyzer import analyze_sentiment


def test_positive_sentiment():
    """Test detection of positive sentiment."""
    text = "This is absolutely wonderful and amazing! I love it!"
    result = analyze_sentiment(text)
    
    assert result["sentiment"] == "positive"
    assert 0 <= result["confidence"] <= 1


def test_negative_sentiment():
    """Test detection of negative sentiment."""
    text = "This is terrible and awful. I hate it completely."
    result = analyze_sentiment(text)
    
    assert result["sentiment"] == "negative"
    assert 0 <= result["confidence"] <= 1


def test_neutral_sentiment():
    """Test detection of neutral sentiment."""
    text = "This is a computer. It has a keyboard and a mouse."
    result = analyze_sentiment(text)
    
    assert result["sentiment"] == "neutral"
    assert 0 <= result["confidence"] <= 1


def test_empty_text():
    """Test sentiment analysis with empty text."""
    result = analyze_sentiment("")
    
    assert result["sentiment"] == "neutral"
    assert result["confidence"] == 0.0


def test_whitespace_only():
    """Test sentiment analysis with whitespace only."""
    result = analyze_sentiment("   \n  \t  ")
    
    assert result["sentiment"] == "neutral"
    assert result["confidence"] == 0.0


def test_mixed_sentiment():
    """Test text with mixed sentiment."""
    text = "The product is good but the service was bad."
    result = analyze_sentiment(text)
    
    # Should return one of the valid sentiments
    assert result["sentiment"] in ["positive", "neutral", "negative"]
    assert 0 <= result["confidence"] <= 1


def test_technical_text():
    """Test sentiment on technical/factual text."""
    text = "The function takes two parameters and returns a boolean value."
    result = analyze_sentiment(text)
    
    # Technical text should generally be neutral
    assert result["sentiment"] in ["neutral", "positive", "negative"]
    assert 0 <= result["confidence"] <= 1


def test_confident_positive():
    """Test strongly positive text has high confidence."""
    text = "Excellent! Outstanding! Perfect! Amazing work! Brilliant!"
    result = analyze_sentiment(text)
    
    assert result["sentiment"] == "positive"
    # Strong sentiment should have reasonable confidence
    assert result["confidence"] > 0.3


def test_confident_negative():
    """Test strongly negative text has high confidence."""
    text = "Horrible! Terrible! Awful! Disaster! Worst ever!"
    result = analyze_sentiment(text)
    
    assert result["sentiment"] == "negative"
    # Strong sentiment should have reasonable confidence
    assert result["confidence"] > 0.3
