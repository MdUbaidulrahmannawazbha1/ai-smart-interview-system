"""
Answer evaluator tests
"""
import pytest
from app.services.answer_evaluator import answer_evaluator


def test_evaluate_good_answer():
    """Test evaluation of a good answer"""
    question = "What is Python?"
    answer = "Python is a high-level, interpreted programming language known for its simplicity and readability."
    
    evaluation = answer_evaluator.evaluate_answer(
        question_id="test-1",
        question_text=question,
        answer_text=answer,
        expected_keywords=["programming", "language", "python"]
    )
    
    assert evaluation.overall_score > 0.3
    assert evaluation.grade in ["excellent", "good", "average", "poor"]
    assert len(evaluation.feedback) > 0


def test_evaluate_poor_answer():
    """Test evaluation of a poor answer"""
    question = "Explain machine learning algorithms"
    answer = "I don't know"
    
    evaluation = answer_evaluator.evaluate_answer(
        question_id="test-2",
        question_text=question,
        answer_text=answer,
        expected_keywords=["algorithm", "learning", "model"]
    )
    
    assert evaluation.overall_score < 0.5
    assert len(evaluation.feedback) > 0


def test_evaluate_answer_with_keywords():
    """Test keyword matching in evaluation"""
    question = "What are the key features of object-oriented programming?"
    answer = "Object-oriented programming includes encapsulation, inheritance, and polymorphism as key concepts."
    
    evaluation = answer_evaluator.evaluate_answer(
        question_id="test-3",
        question_text=question,
        answer_text=answer,
        expected_keywords=["encapsulation", "inheritance", "polymorphism", "object"]
    )
    
    assert evaluation.keyword_match_score > 0.5
    assert evaluation.overall_score > 0.3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
