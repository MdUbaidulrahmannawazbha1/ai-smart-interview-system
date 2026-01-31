"""
Basic tests without heavy ML dependencies
"""
import pytest


def test_imports():
    """Test basic imports work"""
    from app.core.config import settings
    from app.schemas.interview import Question, InterviewRequest
    from app.schemas.evaluation import EvaluationRequest
    
    assert settings.PROJECT_NAME == "AI Smart Interview System"
    assert settings.VERSION == "1.0.0"
    
    # Test schema creation
    question = Question(
        id="test-1",
        text="Test question",
        category="technical",
        difficulty="medium"
    )
    assert question.id == "test-1"


def test_text_utils():
    """Test text utility functions"""
    from app.utils.text_utils import clean_text, extract_keywords, calculate_keyword_match_score
    
    # Test clean_text
    dirty = "  This   has   extra    spaces  "
    clean = clean_text(dirty)
    assert "  " not in clean
    
    # Test extract_keywords
    text = "Python is a programming language"
    keywords = extract_keywords(text)
    assert "python" in keywords
    assert "programming" in keywords
    assert "language" in keywords
    
    # Test keyword matching
    score = calculate_keyword_match_score(
        "Python is a programming language",
        ["python", "programming"]
    )
    assert score > 0.5


def test_question_generator():
    """Test question generation"""
    from app.services.question_generator import question_generator
    
    questions = question_generator.generate_questions(
        position="Python Developer",
        num_questions=3
    )
    
    assert len(questions) == 3
    assert all(hasattr(q, 'id') for q in questions)
    assert all(hasattr(q, 'text') for q in questions)


def test_response_formatter():
    """Test response formatting"""
    from app.utils.response_formatter import success_response, error_response
    
    success = success_response({"key": "value"}, "Test success")
    assert success["status"] == "success"
    assert success["message"] == "Test success"
    assert success["data"]["key"] == "value"
    
    error = error_response("Test error", "ERR001")
    assert error["status"] == "error"
    assert error["message"] == "Test error"
    assert error["error_code"] == "ERR001"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
