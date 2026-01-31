"""
test_evaluator.py

Unit tests for answer evaluation functionality.
"""

import pytest
from app.services.answer_evaluator import evaluate_answer, evaluate_multiple_answers


def test_evaluate_answer_basic():
    """Test basic answer evaluation."""
    question = "What is machine learning?"
    user_answer = "Machine learning is a branch of AI that enables computers to learn from data."
    expected_answer = "Machine learning is an AI technique where systems learn from data without explicit programming."
    
    result = evaluate_answer(question, user_answer, expected_answer)
    
    assert "similarity_percentage" in result
    assert "sentiment" in result
    assert "final_score" in result
    assert "overall_feedback" in result
    assert 0 <= result["final_score"] <= 100
    assert result["sentiment"] in ["positive", "neutral", "negative"]


def test_evaluate_answer_high_similarity():
    """Test evaluation with highly similar answers."""
    question = "What is Python?"
    answer = "Python is a programming language used for web development and data science."
    
    result = evaluate_answer(question, answer, answer)
    
    # Same answer should have 100% similarity
    assert result["similarity_percentage"] > 95
    assert result["final_score"] > 80


def test_evaluate_answer_low_similarity():
    """Test evaluation with dissimilar answers."""
    question = "What is Python?"
    user_answer = "I don't know."
    expected_answer = "Python is a high-level programming language known for readability and versatility."
    
    result = evaluate_answer(question, user_answer, expected_answer)
    
    assert result["similarity_percentage"] < 50
    assert result["final_score"] < 60


def test_evaluate_multiple_answers():
    """Test batch evaluation of multiple answers."""
    qa_pairs = [
        {
            "question": "What is Python?",
            "user_answer": "Python is a programming language.",
            "expected_answer": "Python is a high-level programming language."
        },
        {
            "question": "What is AI?",
            "user_answer": "AI is artificial intelligence.",
            "expected_answer": "AI refers to computer systems that can perform tasks requiring human intelligence."
        }
    ]
    
    result = evaluate_multiple_answers(qa_pairs)
    
    assert "average_score" in result
    assert "evaluations" in result
    assert "total_questions" in result
    assert result["total_questions"] == 2
    assert len(result["evaluations"]) == 2


def test_evaluate_empty_list():
    """Test batch evaluation with empty list."""
    result = evaluate_multiple_answers([])
    
    assert result["average_score"] == 0.0
    assert result["total_questions"] == 0
    assert len(result["evaluations"]) == 0


def test_evaluate_answer_with_positive_sentiment():
    """Test that positive answers are recognized."""
    question = "How do you feel about coding?"
    user_answer = "I absolutely love coding! It's amazing and exciting."
    expected_answer = "I enjoy coding."
    
    result = evaluate_answer(question, user_answer, expected_answer)
    
    # The sentiment should be positive
    assert result["sentiment"] == "positive"


def test_evaluate_answer_with_negative_sentiment():
    """Test that negative answers are recognized."""
    question = "How do you feel about coding?"
    user_answer = "I hate coding. It's terrible and frustrating."
    expected_answer = "I enjoy coding."
    
    result = evaluate_answer(question, user_answer, expected_answer)
    
    # The sentiment should be negative
    assert result["sentiment"] == "negative"
