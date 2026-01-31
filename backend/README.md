# AI Smart Interview System - Backend

FastAPI-based backend for the AI-Powered Smart Interview System.

## Features

- RESTful API for interview question generation
- AI-powered answer evaluation using TF-IDF and cosine similarity
- Sentiment analysis for candidate responses
- Comprehensive scoring engine
- Health check endpoints

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy environment variables:
```bash
cp .env.example .env
```

3. Run the development server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Access API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run tests with pytest:
```bash
pytest tests/ -v
```

## API Endpoints

### Health Check
- `GET /api/v1/health/` - Check service health

### Interview
- `POST /api/v1/interview/question` - Generate interview question
- `POST /api/v1/interview/evaluate` - Evaluate candidate answer

## Architecture

- **API Layer**: FastAPI routes and request/response handling
- **Service Layer**: Business logic and orchestration
- **ML Layer**: Machine learning models and algorithms
- **Utils**: Helper functions and utilities

## Technologies

- FastAPI
- Pydantic for data validation
- scikit-learn for ML operations
- TextBlob for sentiment analysis
- NumPy for numerical operations
