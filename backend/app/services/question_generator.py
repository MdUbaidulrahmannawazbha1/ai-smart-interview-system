"""
question_generator.py

Service layer for generating interview questions in AI-Powered Smart Interview System.
Uses question generation logic to create contextual interview questions.
"""

from typing import Optional, List


def generate_question(
    role: str,
    difficulty: str,
    previous_questions: Optional[List[str]] = None
) -> str:
    """
    Generate an interview question based on job role and difficulty level.
    
    Args:
        role: Job role for the interview (e.g., "Senior Developer", "Product Manager")
        difficulty: Difficulty level - "easy", "medium", or "hard"
        previous_questions: List of previously asked questions for context
        
    Returns:
        str: Generated interview question
        
    Raises:
        Exception: If question generation fails
    """
    try:
        # Simple template-based question generation
        difficulty_mapping = {
            "easy": "Can you explain the basics of",
            "medium": "How do you approach complex problems related to",
            "hard": "How would you design and implement a solution for a challenging scenario in"
        }
        
        question_start = difficulty_mapping.get(
            difficulty.lower(),
            "Can you tell me about your experience with"
        )
        
        question = f"{question_start} {role}?"
        
        return question
        
    except Exception as e:
        raise Exception(f"Question generation failed: {str(e)}")
