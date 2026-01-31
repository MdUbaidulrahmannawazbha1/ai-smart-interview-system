"""
settings.py

Application settings module for AI-Powered Smart Interview System.
Defines configuration settings and environment variables.
"""

from typing import Optional
import os


class Settings:
    """
    Application settings and configuration.
    """
    
    # Application metadata
    APP_NAME: str = "AI-Powered Smart Interview System"
    APP_VERSION: str = "1.0.0"
    
    # API Configuration
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # CORS Configuration
    CORS_ORIGINS: list = ["*"]
    
    # Model Configuration
    TFIDF_MAX_FEATURES: int = 1000
    SIMILARITY_THRESHOLD: float = 0.5
    
    # Scoring Weights
    SIMILARITY_WEIGHT: float = 0.7
    SENTIMENT_WEIGHT: float = 0.3
    
    # Sentiment Scoring
    SENTIMENT_SCORES: dict = {
        "positive": 100.0,
        "neutral": 75.0,
        "negative": 50.0,
    }
    
    # Audio Processing
    MAX_AUDIO_SIZE_MB: int = 25
    SUPPORTED_AUDIO_FORMATS: list = ['.mp3', '.wav', '.ogg', '.flac', '.m4a', '.webm']
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: Optional[str] = os.getenv("LOG_FILE")
    
    # Database (for future use)
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    
    # External API Keys (for future integrations)
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    SPEECH_API_KEY: Optional[str] = os.getenv("SPEECH_API_KEY")


# Global settings instance
settings = Settings()
