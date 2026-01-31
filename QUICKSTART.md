# 🚀 Quick Start Guide

## Prerequisites
- Python 3.8+ installed
- Node.js 16+ installed (for frontend)
- pip and npm available

## Backend Setup (5 minutes)

### 1. Navigate to backend directory
```bash
cd backend
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

**Note**: The system works with minimal dependencies. For full ML features, install:
```bash
# Optional: For sentiment analysis (requires ~500MB download)
pip install transformers torch

# Optional: For audio transcription
pip install speechrecognition pydub
```

### 3. Start the server
```bash
python -m app.main
```

Server will start on: **http://localhost:8000**

API Documentation: **http://localhost:8000/docs**

## Frontend Setup (3 minutes)

### 1. Navigate to frontend directory
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Start development server
```bash
npm run dev
```

Frontend will start on: **http://localhost:5173**

## Test the System

### Using curl
```bash
# Health check
curl http://localhost:8000/health

# Start interview
curl -X POST http://localhost:8000/api/v1/interview/start \
  -H "Content-Type: application/json" \
  -d '{"candidate_name": "John Doe", "position": "Python Developer", "num_questions": 3}'
```

### Using Browser
1. Open http://localhost:5173
2. Enter your name and position
3. Click "Start Interview"
4. Answer the questions
5. View your evaluation and recommendations

### Using Python
```bash
cd backend
python test_api_manual.py
```

## Running Tests

```bash
cd backend
pytest tests/test_basic.py -v
```

## What You Get

✅ **Automated Question Generation** - Dynamic questions based on position
✅ **AI-Powered Evaluation** - Multi-factor scoring with feedback
✅ **Real-time Results** - Instant evaluation and recommendations
✅ **Comprehensive Reports** - Detailed performance analysis

## Next Steps

- 📖 Read [Architecture Documentation](docs/architecture.md)
- 🔌 Explore [API Documentation](http://localhost:8000/docs)
- 🧪 Check [Evaluation Logic](docs/evaluation_logic.md)
- 🎯 Try different positions and questions

---
**Ready in < 10 minutes!** 🎉
