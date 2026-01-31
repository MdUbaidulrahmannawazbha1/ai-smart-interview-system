"""
API endpoint tests
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "service" in data
    assert "version" in data


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data


def test_start_interview():
    """Test starting an interview"""
    request_data = {
        "candidate_name": "John Doe",
        "position": "Python Developer",
        "num_questions": 3
    }
    
    response = client.post("/api/v1/interview/start", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "session_id" in data
    assert "questions" in data
    assert len(data["questions"]) == 3
    
    # Store session_id for later tests
    return data["session_id"]


def test_evaluate_answer():
    """Test answer evaluation"""
    # First create an interview session
    session_id = test_start_interview()
    
    # Get session to get question ID
    session_response = client.get(f"/api/v1/interview/session/{session_id}")
    assert session_response.status_code == 200
    
    session_data = session_response.json()
    question_id = session_data["session"]["questions"][0]["id"]
    
    # Evaluate an answer
    eval_request = {
        "session_id": session_id,
        "question_id": question_id,
        "answer_text": "Python is a high-level programming language that is widely used for web development, data science, and automation."
    }
    
    response = client.post("/api/v1/evaluation/evaluate", json=eval_request)
    assert response.status_code == 200
    
    data = response.json()
    assert "evaluation" in data
    assert data["evaluation"]["overall_score"] >= 0
    assert data["evaluation"]["overall_score"] <= 1


def test_final_evaluation():
    """Test final evaluation"""
    # Create session and evaluate an answer
    session_id = test_start_interview()
    
    session_response = client.get(f"/api/v1/interview/session/{session_id}")
    question_id = session_response.json()["session"]["questions"][0]["id"]
    
    # Submit evaluation
    eval_request = {
        "session_id": session_id,
        "question_id": question_id,
        "answer_text": "This is a test answer with relevant content."
    }
    client.post("/api/v1/evaluation/evaluate", json=eval_request)
    
    # Get final evaluation
    final_request = {"session_id": session_id}
    response = client.post("/api/v1/evaluation/final-evaluation", json=final_request)
    
    assert response.status_code == 200
    data = response.json()
    assert "average_score" in data
    assert "overall_grade" in data
    assert "recommendations" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
