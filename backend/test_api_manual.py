"""
Manual API testing script
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("\n=== Testing Health Endpoint ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

def test_start_interview():
    """Test starting an interview"""
    print("\n=== Testing Start Interview ===")
    data = {
        "candidate_name": "John Doe",
        "position": "Python Developer",
        "num_questions": 3
    }
    response = requests.post(f"{BASE_URL}/api/v1/interview/start", json=data)
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response: {json.dumps(result, indent=2)}")
    return result.get("session_id"), result.get("questions", [])

def test_evaluate_answer(session_id, question):
    """Test answer evaluation"""
    print("\n=== Testing Answer Evaluation ===")
    data = {
        "session_id": session_id,
        "question_id": question["id"],
        "answer_text": "Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms including procedural, object-oriented, and functional programming."
    }
    response = requests.post(f"{BASE_URL}/api/v1/evaluation/evaluate", json=data)
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response: {json.dumps(result, indent=2)}")
    return response.status_code == 200

def test_final_evaluation(session_id):
    """Test final evaluation"""
    print("\n=== Testing Final Evaluation ===")
    data = {"session_id": session_id}
    response = requests.post(f"{BASE_URL}/api/v1/evaluation/final-evaluation", json=data)
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Response: {json.dumps(result, indent=2)}")
    return response.status_code == 200

if __name__ == "__main__":
    try:
        # Test health
        if not test_health():
            print("Health check failed!")
            exit(1)
        
        # Test interview flow
        session_id, questions = test_start_interview()
        if not session_id or not questions:
            print("Failed to start interview!")
            exit(1)
        
        # Test evaluation
        if questions:
            test_evaluate_answer(session_id, questions[0])
        
        # Test final evaluation
        test_final_evaluation(session_id)
        
        print("\n=== All Tests Passed! ===")
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to server. Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"\nError: {e}")
