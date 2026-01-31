# 📁 Project Structure

```
ai-smart-interview-system/
│
├── 📄 README.md                      # Main project documentation
├── 📄 QUICKSTART.md                  # Quick start guide
├── 📄 IMPLEMENTATION_SUMMARY.md      # Implementation details
├── 📄 .gitignore                     # Git ignore rules
│
├── 📂 backend/                       # FastAPI Backend
│   ├── 📄 requirements.txt           # Python dependencies
│   ├── 📄 .env.example               # Environment variables template
│   ├── 📄 README.md                  # Backend documentation
│   ├── 📄 test_api_manual.py         # Manual API testing script
│   │
│   ├── 📂 app/                       # Main application
│   │   ├── 📄 main.py                # FastAPI app entry point
│   │   │
│   │   ├── 📂 api/                   # API layer
│   │   │   ├── 📄 __init__.py
│   │   │   └── 📂 routes/            # API endpoints
│   │   │       ├── 📄 __init__.py
│   │   │       ├── 📄 health.py      # Health check endpoints
│   │   │       ├── 📄 interview.py   # Interview management
│   │   │       └── 📄 evaluation.py  # Evaluation endpoints
│   │   │
│   │   ├── 📂 core/                  # Core configuration
│   │   │   ├── 📄 config.py          # Settings management
│   │   │   ├── 📄 settings.py        # Settings export
│   │   │   └── 📄 logger.py          # Logging configuration
│   │   │
│   │   ├── 📂 schemas/               # Pydantic schemas
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 interview.py       # Interview data models
│   │   │   ├── 📄 evaluation.py      # Evaluation data models
│   │   │   └── 📄 feedback.py        # Feedback data models
│   │   │
│   │   ├── 📂 services/              # Business logic
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 question_generator.py    # Question generation
│   │   │   ├── 📄 answer_evaluator.py      # Answer evaluation
│   │   │   ├── 📄 sentiment_analyzer.py    # Sentiment analysis
│   │   │   ├── 📄 scoring_engine.py        # Score calculation
│   │   │   └── 📄 speech_to_text.py        # Audio transcription
│   │   │
│   │   ├── 📂 ml/                    # ML utilities
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 tfidf_vectorizer.py      # TF-IDF implementation
│   │   │   ├── 📄 cosine_similarity.py     # Similarity calculation
│   │   │   └── 📄 model_loader.py          # ML model management
│   │   │
│   │   ├── 📂 utils/                 # Helper functions
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 text_utils.py      # Text processing
│   │   │   ├── 📄 audio_utils.py     # Audio processing
│   │   │   └── 📄 response_formatter.py    # Response formatting
│   │   │
│   │   └── 📂 constants/             # Constants
│   │       ├── 📄 __init__.py
│   │       └── 📄 messages.py        # Messages and constants
│   │
│   └── 📂 tests/                     # Test suite
│       ├── 📄 test_basic.py          # Basic functionality tests
│       ├── 📄 test_api.py            # API endpoint tests
│       ├── 📄 test_evaluator.py      # Evaluator tests
│       └── 📄 test_sentiment.py      # Sentiment analysis tests
│
├── 📂 frontend/                      # React Frontend
│   ├── 📄 package.json               # Node.js dependencies
│   ├── 📄 vite.config.js             # Vite configuration
│   ├── 📄 index.html                 # HTML entry point
│   ├── 📄 README.md                  # Frontend documentation
│   │
│   └── 📂 src/                       # Source files
│       ├── 📄 main.jsx               # React entry point
│       └── 📄 App.jsx                # Main App component
│
└── 📂 docs/                          # Documentation
    ├── 📄 architecture.md            # System architecture
    ├── 📄 api_flow.md                # API flow documentation
    └── 📄 evaluation_logic.md        # Evaluation algorithm
```

## 📊 Statistics

### Backend
- **Total Files**: 44 Python files
- **Lines of Code**: ~3,000+ lines
- **API Endpoints**: 8 endpoints
- **Test Coverage**: 4 test files

### Frontend
- **Framework**: React 18
- **Components**: 1 main component
- **Build Tool**: Vite

### Documentation
- **Guides**: 6 documentation files
- **READMEs**: 4 README files
- **Examples**: Complete API examples

## 🔑 Key Components

### Backend Services
1. **Question Generator** - Generates interview questions based on position
2. **Answer Evaluator** - Evaluates answers using ML algorithms
3. **Sentiment Analyzer** - Analyzes answer confidence and tone
4. **Scoring Engine** - Calculates overall performance scores

### ML/NLP Features
1. **TF-IDF Vectorization** - Text representation
2. **Cosine Similarity** - Semantic similarity calculation
3. **Sentiment Analysis** - Confidence assessment (optional)
4. **Keyword Extraction** - Technical term detection

### API Routes
1. **Health** - System status
2. **Interview Management** - Start/end sessions
3. **Evaluation** - Answer evaluation
4. **Final Report** - Comprehensive results

## 🎯 Design Patterns

- **Singleton**: Model loader, service instances
- **Factory**: Question generation
- **Strategy**: Multiple evaluation metrics
- **Repository**: In-memory data storage
- **Dependency Injection**: Service composition

## 🔒 Security Features

- CORS configuration
- Input validation (Pydantic)
- Error handling
- Logging system
- Environment variables

## 🚀 Deployment Ready

- Modular architecture
- Configuration management
- Error handling
- Logging
- Testing suite
- Documentation
