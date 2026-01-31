"""
Sentiment analysis service
"""
from typing import Dict
from app.ml.model_loader import model_loader
from app.core.logger import logger


class SentimentAnalyzer:
    """Analyze sentiment of text"""
    
    def __init__(self):
        self.pipeline = None
    
    def _get_pipeline(self):
        """Get or load sentiment pipeline"""
        if self.pipeline is None:
            self.pipeline = model_loader.get_sentiment_pipeline()
        return self.pipeline
    
    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment of text
        
        Args:
            text: Input text
            
        Returns:
            Dictionary with sentiment label and score
        """
        try:
            pipeline = self._get_pipeline()
            
            # Truncate text if too long (model max length is usually 512 tokens)
            max_length = 500
            if len(text) > max_length:
                text = text[:max_length]
            
            # Run sentiment analysis
            result = pipeline(text)[0]
            
            label = result['label']  # POSITIVE or NEGATIVE
            score = result['score']  # Confidence score
            
            # Convert to normalized sentiment score (0 to 1, where 1 is most positive)
            if label == 'POSITIVE':
                sentiment_score = 0.5 + (score * 0.5)  # Map 0-1 confidence to 0.5-1.0
            else:
                sentiment_score = 0.5 - (score * 0.5)  # Map 0-1 confidence to 0.5-0.0
            
            logger.debug(f"Sentiment analysis: {label} ({score:.2f}) -> {sentiment_score:.2f}")
            
            return {
                "label": label,
                "confidence": score,
                "sentiment_score": sentiment_score
            }
        
        except Exception as e:
            logger.error(f"Error in sentiment analysis: {str(e)}")
            # Return neutral sentiment on error
            return {
                "label": "NEUTRAL",
                "confidence": 0.5,
                "sentiment_score": 0.5
            }
    
    def get_sentiment_score(self, text: str) -> float:
        """
        Get normalized sentiment score
        
        Args:
            text: Input text
            
        Returns:
            Sentiment score (0 to 1)
        """
        result = self.analyze_sentiment(text)
        return result["sentiment_score"]


# Global sentiment analyzer instance
sentiment_analyzer = SentimentAnalyzer()
