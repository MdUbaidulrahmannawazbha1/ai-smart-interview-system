"""
sentiment_analyzer.py

Service layer for sentiment analysis in AI-Powered Smart Interview System. 
Analyzes the emotional tone of candidate responses using NLP techniques.
"""

from textblob import TextBlob
from typing import Dict, Any


def analyze_sentiment(text: str) -> Dict[str, Any]:
    """
    Analyze the sentiment of a given text. 
    
    Uses TextBlob polarity analysis to determine emotional tone.
    Polarity ranges from -1 (negative) to +1 (positive).
    
    Args:
        text:   The text to analyze for sentiment
        
    Returns: 
        dict: Contains 'sentiment' (positive/neutral/negative) and 
              'confidence' (0-1 scale)
              
    Raises:
        Exception: If sentiment analysis fails
    """
    try:
        # Handle empty or whitespace-only text
        if not text or not text.strip():
            return {
                "sentiment": "neutral",
                "confidence": 0.0,
            }
        
        # Analyze text using TextBlob
        blob = TextBlob(text)
        # Extract polarity value (TextBlob.sentiment returns a named tuple)
        polarity_value: Any = getattr(blob.sentiment, 'polarity', 0.0)
        polarity = float(polarity_value)
        
        # Determine sentiment category based on polarity
        if polarity > 0.1: 
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        # Calculate confidence score (absolute polarity normalized)
        confidence = min(abs(polarity), 1.0)
        
        return {
            "sentiment": sentiment,
            "confidence": round(confidence, 2),
        }
        
    except Exception as e:
        raise Exception(f"Sentiment analysis failed: {str(e)}")