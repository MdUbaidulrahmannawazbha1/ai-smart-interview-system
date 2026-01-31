"""
TF-IDF Vectorizer for text similarity
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List
import numpy as np


class TFIDFVectorizer:
    """TF-IDF Vectorizer wrapper"""
    
    def __init__(self, max_features: int = 5000):
        """
        Initialize TF-IDF vectorizer
        
        Args:
            max_features: Maximum number of features
        """
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            stop_words='english',
            lowercase=True,
            ngram_range=(1, 2)
        )
        self.is_fitted = False
    
    def fit(self, texts: List[str]):
        """
        Fit the vectorizer on texts
        
        Args:
            texts: List of text documents
        """
        self.vectorizer.fit(texts)
        self.is_fitted = True
    
    def transform(self, texts: List[str]) -> np.ndarray:
        """
        Transform texts to TF-IDF vectors
        
        Args:
            texts: List of text documents
            
        Returns:
            TF-IDF matrix
        """
        if not self.is_fitted:
            self.fit(texts)
        return self.vectorizer.transform(texts).toarray()
    
    def fit_transform(self, texts: List[str]) -> np.ndarray:
        """
        Fit and transform texts
        
        Args:
            texts: List of text documents
            
        Returns:
            TF-IDF matrix
        """
        self.fit(texts)
        return self.transform(texts)
