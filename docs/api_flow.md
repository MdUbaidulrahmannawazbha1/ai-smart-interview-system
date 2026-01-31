# API Flow

## Interview Workflow

### 1. Start Interview
**Endpoint**: `POST /api/v1/interview/start`

**Request**:
```json
{
  "candidate_name": "John Doe",
  "position": "Python Developer",
  "num_questions": 5
}
```

**Response**:
```json
{
  "session_id": "uuid",
  "questions": [
    {
      "id": "q-uuid",
      "text": "Question text",
      "category": "technical",
      "difficulty": "medium",
      "expected_keywords": ["keyword1", "keyword2"]
    }
  ],
  "message": "Interview session created successfully"
}
```

### 2. Submit Answer
**Endpoint**: `POST /api/v1/interview/submit-answer`

**Request**:
```json
{
  "question_id": "q-uuid",
  "text": "Answer text",
  "audio_url": "optional-url"
}
```

### 3. Evaluate Answer
**Endpoint**: `POST /api/v1/evaluation/evaluate`

**Request**:
```json
{
  "session_id": "session-uuid",
  "question_id": "q-uuid",
  "answer_text": "Answer text"
}
```

**Response**:
```json
{
  "evaluation": {
    "question_id": "q-uuid",
    "similarity_score": 0.75,
    "sentiment_score": 0.82,
    "keyword_match_score": 0.68,
    "overall_score": 0.74,
    "feedback": "Good answer...",
    "grade": "good"
  }
}
```

### 4. Get Final Evaluation
**Endpoint**: `POST /api/v1/evaluation/final-evaluation`

**Request**:
```json
{
  "session_id": "session-uuid"
}
```

**Response**:
```json
{
  "session_id": "uuid",
  "evaluations": [...],
  "average_score": 0.72,
  "total_questions": 5,
  "answered_questions": 5,
  "overall_grade": "good",
  "summary": "Good performance overall...",
  "recommendations": ["Recommendation 1", "Recommendation 2"]
}
```

### 5. Health Check
**Endpoint**: `GET /health`

**Response**:
```json
{
  "status": "healthy",
  "service": "AI Smart Interview System",
  "version": "1.0.0"
}
```

## Error Responses

All endpoints may return error responses in this format:

```json
{
  "detail": "Error message"
}
```

Common HTTP status codes:
- 200: Success
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error
