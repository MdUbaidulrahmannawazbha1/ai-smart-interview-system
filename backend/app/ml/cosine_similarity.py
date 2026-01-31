"""
Cosine similarity computation
"""
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine_similarity
import numpy as np
from typing import List


def cosine_similarity(vector1: np.ndarray, vector2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors
    
    Args:
        vector1: First vector
        vector2: Second vector
        
    Returns:
        Cosine similarity score (0 to 1)
    """
    if vector1.ndim == 1:
        vector1 = vector1.reshape(1, -1)
    if vector2.ndim == 1:
        vector2 = vector2.reshape(1, -1)
    
    similarity = sklearn_cosine_similarity(vector1, vector2)[0][0]
    return float(similarity)


def batch_cosine_similarity(vectors: List[np.ndarray], reference_vector: np.ndarray) -> List[float]:
    """
    Calculate cosine similarity between multiple vectors and a reference
    
    Args:
        vectors: List of vectors
        reference_vector: Reference vector
        
    Returns:
        List of similarity scores
    """
    if reference_vector.ndim == 1:
        reference_vector = reference_vector.reshape(1, -1)
    
    similarities = []
    for vector in vectors:
        if vector.ndim == 1:
            vector = vector.reshape(1, -1)
        sim = sklearn_cosine_similarity(vector, reference_vector)[0][0]
        similarities.append(float(sim))
    
    return similarities
