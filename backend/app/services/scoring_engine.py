"""
scoring_engine.py

Service layer for final score calculation in AI-Powered Smart Interview System. 
Combines multiple evaluation signals into a single performance score.
"""

from typing import Dict, Any


def calculate_final_score(
    similarity_percentage: float,
    sentiment_label: str,
    sentiment_confidence: float
) -> Dict[str, Any]: 
    """
    Calculate the final interview performance score.
    
    Combines similarity score (70% weight) and sentiment analysis (30% weight)
    to produce a comprehensive performance evaluation.
    
    Args:
        similarity_percentage:  Answer similarity score (0-100)
        sentiment_label:  Sentiment category (positive, neutral, negative)
        sentiment_confidence: Confidence of sentiment prediction (0-1)
        
    Returns:
        dict: Contains 'final_score' (0-100) and 'overall_feedback' (string)
    """
    # Similarity contribution (70% weight)
    similarity_contribution = similarity_percentage * 0.7
    
    # Sentiment contribution (30% weight)
    sentiment_score = _calculate_sentiment_score(
        sentiment_label, 
        sentiment_confidence
    )
    sentiment_contribution = sentiment_score * 0.3
    
    # Calculate final score
    final_score = similarity_contribution + sentiment_contribution
    
    # Ensure score is within valid range
    final_score = max(0.0, min(100.0, final_score))
    
    # Generate overall feedback
    overall_feedback = _generate_feedback(final_score)
    
    return {
        "final_score":  round(final_score, 2),
        "overall_feedback": overall_feedback,
    }


def _calculate_sentiment_score(sentiment_label: str, confidence: float) -> float:
    """
    Convert sentiment label and confidence into a numeric score.
    
    Args:
        sentiment_label:  Sentiment category (positive, neutral, negative)
        confidence: Confidence level (0-1)
        
    Returns:
        float:  Sentiment score (0-100)
    """
    # Base scores for each sentiment category
    sentiment_base_scores = {
        "positive": 100.0,
        "neutral":  75.0,
        "negative":  50.0,
    }
    
    # Get base score for sentiment label
    base_score = sentiment_base_scores.get(sentiment_label. lower(), 75.0)
    
    # Weight by confidence (low confidence reduces impact)
    weighted_score = base_score * confidence + 75.0 * (1 - confidence)
    
    return weighted_score


def _generate_feedback(final_score: float) -> str:
    """
    Generate overall feedback message based on final score.
    
    Args:
        final_score: Final interview score (0-100)
        
    Returns: 
        str: Feedback message
    """
    if final_score >= 80:
        return "Excellent performance"
    elif final_score >= 60:
        return "Good performance, room for improvement"
    else: 
        return "Needs significant improvement"