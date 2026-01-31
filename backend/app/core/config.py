"""
config.py

Configuration management module for AI-Powered Smart Interview System.
Provides utilities for loading and validating configuration.
"""

from typing import Dict, Any
import os


def load_config() -> Dict[str, Any]:
    """
    Load application configuration from environment and defaults.
    
    Returns:
        dict: Configuration dictionary
    """
    config = {
        "app": {
            "name": "AI-Powered Smart Interview System",
            "version": "1.0.0",
            "debug": os.getenv("DEBUG", "False").lower() == "true",
        },
        "api": {
            "host": os.getenv("API_HOST", "0.0.0.0"),
            "port": int(os.getenv("API_PORT", "8000")),
            "prefix": "/api/v1",
        },
        "ml": {
            "tfidf_max_features": 1000,
            "similarity_threshold": 0.5,
            "similarity_weight": 0.7,
            "sentiment_weight": 0.3,
        },
        "logging": {
            "level": os.getenv("LOG_LEVEL", "INFO"),
            "file": os.getenv("LOG_FILE"),
        },
    }
    
    return config


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate configuration values.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        bool: True if configuration is valid
        
    Raises:
        ValueError: If configuration is invalid
    """
    # Validate ML weights sum to 1.0
    ml_config = config.get("ml", {})
    similarity_weight = ml_config.get("similarity_weight", 0)
    sentiment_weight = ml_config.get("sentiment_weight", 0)
    
    if not (0.99 <= similarity_weight + sentiment_weight <= 1.01):
        raise ValueError("ML weights (similarity + sentiment) must sum to 1.0")
    
    # Validate port number
    api_port = config.get("api", {}).get("port", 0)
    if not (1 <= api_port <= 65535):
        raise ValueError("API port must be between 1 and 65535")
    
    return True


# Load and validate configuration on module import
app_config = load_config()
validate_config(app_config)
