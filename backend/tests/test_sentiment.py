"""
Sentiment analyzer tests
"""
import pytest
from app.services.sentiment_analyzer import sentiment_analyzer


def test_positive_sentiment():
    """Test positive sentiment detection"""
    text = "This is an excellent and wonderful solution that works perfectly!"
    
    result = sentiment_analyzer.analyze_sentiment(text)
    
    assert result["sentiment_score"] > 0.5
    assert "label" in result
    assert "confidence" in result


def test_negative_sentiment():
    """Test negative sentiment detection"""
    text = "This is terrible and doesn't work at all. Very disappointing."
    
    result = sentiment_analyzer.analyze_sentiment(text)
    
    assert result["sentiment_score"] < 0.5


def test_neutral_sentiment():
    """Test neutral text"""
    text = "The function returns a value."
    
    result = sentiment_analyzer.analyze_sentiment(text)
    
    assert 0.3 <= result["sentiment_score"] <= 0.7


def test_get_sentiment_score():
    """Test getting sentiment score directly"""
    text = "This is great and I'm happy with the results!"
    
    score = sentiment_analyzer.get_sentiment_score(text)
    
    assert isinstance(score, float)
    assert 0 <= score <= 1
    assert score > 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
