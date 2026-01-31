"""
tfidf_vectorizer.py

ML layer for TF-IDF vectorization in AI-Powered Smart Interview System. 
Converts text into numerical vectors for similarity computation.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from typing import Tuple
import numpy as np


def vectorize_texts(text_1: str, text_2: str) -> Tuple[np.ndarray, np. ndarray]:
    """
    Convert two text inputs into TF-IDF vectors. 
    
    Uses TF-IDF (Term Frequency-Inverse Document Frequency) to transform
    text into numerical feature vectors that capture word importance.
    
    Args:
        text_1: First text to vectorize
        text_2: Second text to vectorize
        
    Returns:
        tuple: (vector_1, vector_2) as numpy arrays
        
    Raises:
        Exception: If vectorization fails
    """
    try: 
        # Handle empty or whitespace-only texts
        if not text_1 or not text_1.strip():
            text_1 = " "
        if not text_2 or not text_2.strip():
            text_2 = " "
        
        # Initialize TF-IDF vectorizer
        vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words='english',
            max_features=1000,
        )
        
        # Fit and transform both texts together
        tfidf_matrix = vectorizer.fit_transform([text_1, text_2])
        
        # Extract individual vectors
        vector_1 = tfidf_matrix.getrow(0).toarray().flatten()
        vector_2 = tfidf_matrix.getrow(1).toarray().flatten()
        
        return vector_1, vector_2
        
    except Exception as e:
        raise Exception(f"TF-IDF vectorization failed: {str(e)}")