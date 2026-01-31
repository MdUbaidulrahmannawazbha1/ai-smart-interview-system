"""
model_loader.py

ML model loading and management module for AI-Powered Smart Interview System.
Provides utilities for loading and caching ML models.
"""

from typing import Any, Optional
import pickle
import os


class ModelLoader:
    """
    Singleton class for loading and caching ML models.
    """
    _instance = None
    _models = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
        return cls._instance
    
    def load_model(self, model_path: str, model_name: str) -> Any:
        """
        Load a model from disk and cache it.
        
        Args:
            model_path: Path to the model file
            model_name: Unique identifier for the model
            
        Returns:
            Loaded model object
            
        Raises:
            FileNotFoundError: If model file doesn't exist
            Exception: If loading fails
        """
        # Check if model is already cached
        if model_name in self._models:
            return self._models[model_name]
        
        # Verify file exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        
        try:
            # Load model using pickle
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            
            # Cache the model
            self._models[model_name] = model
            
            return model
            
        except Exception as e:
            raise Exception(f"Failed to load model {model_name}: {str(e)}")
    
    def get_model(self, model_name: str) -> Optional[Any]:
        """
        Get a cached model by name.
        
        Args:
            model_name: Unique identifier for the model
            
        Returns:
            Model object if cached, None otherwise
        """
        return self._models.get(model_name)
    
    def clear_cache(self):
        """
        Clear all cached models from memory.
        """
        self._models.clear()
    
    def is_loaded(self, model_name: str) -> bool:
        """
        Check if a model is loaded and cached.
        
        Args:
            model_name: Unique identifier for the model
            
        Returns:
            bool: True if model is loaded
        """
        return model_name in self._models


# Global instance
model_loader = ModelLoader()
