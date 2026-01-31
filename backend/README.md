# AI Smart Interview System - Backend

FastAPI-based backend server for the AI Smart Interview System.

## Features

- RESTful API with FastAPI
- Interview question generation
- Answer evaluation using ML
- Speech-to-text processing
- Sentiment analysis
- Automated scoring engine

## API Endpoints

### Health Check
- `GET /api/v1/health` - Check system health

### Interview
- Interview-related endpoints under `/api/v1/interview`

### Evaluation
- Evaluation-related endpoints under `/api/v1/evaluation`

## Running the Backend

### Quick Start
From the project root:
```bash
./start_backend.sh
```

### Manual Start
```bash
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
backend/
├── app/
│   ├── api/          # API routes and endpoints
│   ├── core/         # Core configurations
│   ├── ml/           # Machine learning models
│   ├── schemas/      # Pydantic data models
│   ├── services/     # Business logic
│   ├── utils/        # Utility functions
│   └── main.py       # Application entry point
└── tests/            # Test suite
```

## Dependencies

See `requirements.txt` for full list of dependencies.
