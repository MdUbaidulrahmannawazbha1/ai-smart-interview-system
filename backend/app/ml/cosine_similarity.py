"""
cosine_similarity.py

ML layer for cosine similarity computation in AI-Powered Smart Interview System. 
Calculates similarity between vector representations of texts. 
"""

from sklearn.metrics. pairwise import cosine_similarity
import numpy as np


def compute_cosine_similarity(vector_1: np.ndarray, vector_2: np.ndarray) -> float:
    """
    Compute cosine similarity between two vectors.
    
    Cosine similarity measures the cosine of the angle between two vectors,
    producing a value between 0 (completely dissimilar) and 1 (identical).
    
    Args:
        vector_1: First vector as numpy array
        vector_2: Second vector as numpy array
        
    Returns:
        float:  Cosine similarity score (0-1)
        
    Raises: 
        Exception: If similarity computation fails
    """
    try:
        # Reshape vectors to 2D arrays (required by sklearn)
        vec_1 = vector_1.reshape(1, -1)
        vec_2 = vector_2.reshape(1, -1)
        
        # Compute cosine similarity
        similarity_matrix = cosine_similarity(vec_1, vec_2)
        
        # Extract scalar similarity value
        similarity_score = similarity_matrix[0][0]
        
        # Ensure score is within valid range [0, 1]
        similarity_score = max(0.0, min(1.0, float(similarity_score)))
        
        return similarity_score
        
    except Exception as e:
        raise Exception(f"Cosine similarity computation failed: {str(e)}")