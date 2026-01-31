# AI Smart Interview System - Backend

## Overview

FastAPI-based backend for the AI Smart Interview System, providing RESTful APIs for interview management and AI-powered answer evaluation.

## Features

- 🎯 Automated interview question generation
- 🤖 AI-powered answer evaluation using NLP
- 📊 Multi-factor scoring (similarity, keywords, sentiment)
- 📈 Comprehensive feedback and recommendations
- 🎤 Speech-to-text support (future enhancement)

## Technology Stack

- **Framework**: FastAPI
- **ML/NLP**: Transformers (Hugging Face), scikit-learn
- **Configuration**: Pydantic Settings
- **Testing**: pytest

## Installation

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set up environment** (optional):
```bash
cp .env.example .env
# Edit .env with your configurations
```

## Running the Server

### Development Mode
```bash
cd backend
python -m app.main
```

Or using uvicorn directly:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing

Run all tests:
```bash
pytest backend/tests/ -v
```

Run specific test file:
```bash
pytest backend/tests/test_api.py -v
```

## Project Structure

```
backend/
├── app/
│   ├── api/              # API routes
│   │   └── routes/       # Endpoint definitions
│   ├── core/             # Core configuration
│   ├── ml/               # ML models and utilities
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   ├── utils/            # Helper functions
│   └── main.py           # FastAPI app
├── tests/                # Test files
└── requirements.txt      # Dependencies
```

## API Endpoints

### Health Check
- `GET /health` - Check API health

### Interview
- `POST /api/v1/interview/start` - Start new interview
- `POST /api/v1/interview/submit-answer` - Submit answer
- `GET /api/v1/interview/session/{session_id}` - Get session details
- `POST /api/v1/interview/end/{session_id}` - End interview

### Evaluation
- `POST /api/v1/evaluation/evaluate` - Evaluate single answer
- `POST /api/v1/evaluation/final-evaluation` - Get final evaluation
- `GET /api/v1/evaluation/session/{session_id}/evaluations` - Get all evaluations

## Configuration

Key settings in `app/core/config.py`:
- `API_V1_PREFIX`: API route prefix
- `MODEL_NAME`: Sentiment analysis model
- `MAX_QUESTIONS`: Maximum questions per interview
- Scoring thresholds for grading

## ML Models

### Sentiment Analysis
- Model: `distilbert-base-uncased-finetuned-sst-2-english`
- Purpose: Analyze answer confidence and tone

### Text Similarity
- Method: TF-IDF + Cosine Similarity
- Purpose: Measure semantic similarity

## Development

To add new features:
1. Define schemas in `app/schemas/`
2. Implement business logic in `app/services/`
3. Create API routes in `app/api/routes/`
4. Add tests in `tests/`
