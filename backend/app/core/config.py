"""
Application configuration settings
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings"""
    
    # API Settings
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "AI Smart Interview System"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # CORS Settings
    CORS_ORIGINS: list = ["*"]
    
    # ML Model Settings
    MODEL_NAME: str = "distilbert-base-uncased-finetuned-sst-2-english"
    MAX_SEQUENCE_LENGTH: int = 512
    
    # Interview Settings
    MAX_QUESTIONS: int = 10
    TIME_LIMIT_PER_QUESTION: int = 300  # seconds
    
    # Scoring Thresholds
    MIN_SIMILARITY_SCORE: float = 0.3
    EXCELLENT_THRESHOLD: float = 0.8
    GOOD_THRESHOLD: float = 0.6
    AVERAGE_THRESHOLD: float = 0.4
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
