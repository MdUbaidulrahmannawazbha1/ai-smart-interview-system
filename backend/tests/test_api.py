"""
test_api.py

Unit tests for API endpoints in AI-Powered Smart Interview System.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns correct response."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"
    assert "AI-Powered Smart Interview System" in data["service"]


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "AI-Powered Smart Interview System" in data["service"]


def test_generate_question():
    """Test interview question generation endpoint."""
    payload = {
        "role": "Senior Software Engineer",
        "difficulty": "medium"
    }
    response = client.post("/api/v1/interview/question", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "question" in data
    assert data["role"] == payload["role"]
    assert data["difficulty"] == payload["difficulty"]
    assert len(data["question"]) > 0


def test_generate_question_with_previous():
    """Test question generation with previous questions context."""
    payload = {
        "role": "Product Manager",
        "difficulty": "hard",
        "previous_questions": ["What is your experience?"]
    }
    response = client.post("/api/v1/interview/question", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "question" in data
    assert len(data["question"]) > 0


def test_evaluate_answer():
    """Test answer evaluation endpoint."""
    payload = {
        "question": "What is Python?",
        "user_answer": "Python is a high-level programming language known for its simplicity and readability.",
        "expected_answer": "Python is a versatile, high-level programming language that emphasizes code readability."
    }
    response = client.post("/api/v1/interview/evaluate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "similarity_percentage" in data
    assert "sentiment" in data
    assert "final_score" in data
    assert "overall_feedback" in data
    assert 0 <= data["similarity_percentage"] <= 100
    assert 0 <= data["final_score"] <= 100
    assert data["sentiment"]["label"] in ["positive", "neutral", "negative"]


def test_evaluate_empty_answer():
    """Test evaluation with empty answer."""
    payload = {
        "question": "What is Python?",
        "user_answer": "",
        "expected_answer": "Python is a programming language."
    }
    response = client.post("/api/v1/interview/evaluate", json=payload)
    # Should still return a response, even if score is low
    assert response.status_code == 200
    data = response.json()
    assert "final_score" in data


def test_evaluate_identical_answers():
    """Test evaluation with identical user and expected answers."""
    answer_text = "Python is a high-level, interpreted programming language."
    payload = {
        "question": "What is Python?",
        "user_answer": answer_text,
        "expected_answer": answer_text
    }
    response = client.post("/api/v1/interview/evaluate", json=payload)
    assert response.status_code == 200
    data = response.json()
    # Identical answers should have high similarity
    assert data["similarity_percentage"] > 90


def test_missing_required_fields():
    """Test API validation with missing required fields."""
    payload = {
        "role": "Developer"
        # Missing 'difficulty' field
    }
    response = client.post("/api/v1/interview/question", json=payload)
    assert response.status_code == 422  # Validation error
