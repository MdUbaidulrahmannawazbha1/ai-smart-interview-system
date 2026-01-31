"""
ML Model loader
"""
from app.core.logger import logger
from app.core.config import settings
from typing import Optional

try:
    from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    logger.warning("transformers library not available. Sentiment analysis will use fallback.")


class ModelLoader:
    """Singleton model loader"""
    
    _instance: Optional['ModelLoader'] = None
    _sentiment_pipeline = None
    _tokenizer = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
        return cls._instance
    
    def load_sentiment_model(self):
        """
        Load sentiment analysis model
        
        Returns:
            Sentiment analysis pipeline or None
        """
        if not TRANSFORMERS_AVAILABLE:
            logger.warning("Transformers not available, sentiment analysis will use fallback")
            return None
            
        if self._sentiment_pipeline is None:
            try:
                logger.info(f"Loading sentiment model: {settings.MODEL_NAME}")
                self._sentiment_pipeline = pipeline(
                    "sentiment-analysis",
                    model=settings.MODEL_NAME
                )
                logger.info("Sentiment model loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load sentiment model: {str(e)}")
                raise
        
        return self._sentiment_pipeline
    
    def load_tokenizer(self):
        """
        Load tokenizer
        
        Returns:
            Tokenizer instance or None
        """
        if not TRANSFORMERS_AVAILABLE:
            logger.warning("Transformers not available")
            return None
            
        if self._tokenizer is None:
            try:
                logger.info(f"Loading tokenizer: {settings.MODEL_NAME}")
                self._tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME)
                logger.info("Tokenizer loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load tokenizer: {str(e)}")
                raise
        
        return self._tokenizer
    
    def get_sentiment_pipeline(self):
        """Get or load sentiment pipeline"""
        if self._sentiment_pipeline is None:
            return self.load_sentiment_model()
        return self._sentiment_pipeline


# Global model loader instance
model_loader = ModelLoader()
