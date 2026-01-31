# AI Smart Interview System

AI Smart Interview System is an intelligent interview platform that leverages artificial intelligence to conduct, evaluate, and provide feedback on technical interviews. The system combines speech recognition, natural language processing, and machine learning to create an automated interview experience.

## 🌟 Features

- **Automated Question Generation**: Dynamic question generation based on job position
- **AI-Powered Evaluation**: Multi-factor scoring using NLP and ML models
- **Real-time Feedback**: Instant evaluation and constructive feedback
- **Sentiment Analysis**: Assess confidence and communication quality
- **Comprehensive Reports**: Detailed performance analysis and recommendations
- **User-Friendly Interface**: Clean, intuitive React-based UI

## 🏗️ Architecture

The system consists of two main components:

### Backend (FastAPI)
- RESTful API for interview management
- AI/ML models for evaluation
- Question generation engine
- Scoring and feedback system

### Frontend (React)
- Interactive interview interface
- Real-time progress tracking
- Results visualization
- Responsive design

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- pip and npm

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the server
python -m app.main
```

The API will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The app will be available at `http://localhost:5173`

## 📚 Documentation

- [Architecture](docs/architecture.md) - System design and components
- [API Flow](docs/api_flow.md) - API endpoints and request/response formats
- [Evaluation Logic](docs/evaluation_logic.md) - Scoring algorithms and methodology
- [Backend README](backend/README.md) - Backend setup and development
- [Frontend README](frontend/README.md) - Frontend setup and development

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Test Coverage

- API endpoint tests
- Answer evaluation tests
- Sentiment analysis tests
- Service layer tests

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI
- **ML/NLP**: 
  - Transformers (Hugging Face)
  - scikit-learn
  - SpeechRecognition
- **Configuration**: Pydantic

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **HTTP Client**: Axios

## 📊 Evaluation System

The system uses a sophisticated multi-factor evaluation approach:

### Scoring Components (Total = 100%)
- **Semantic Similarity (40%)**: TF-IDF + Cosine Similarity
- **Keyword Match (40%)**: Technical term coverage
- **Sentiment Analysis (20%)**: Confidence and clarity

### Grading Scale
- **Excellent**: ≥80% - Outstanding performance
- **Good**: 60-79% - Solid understanding
- **Average**: 40-59% - Basic understanding
- **Poor**: <40% - Needs improvement

## 🎯 Use Cases

1. **Technical Screening**: Automate initial candidate screening
2. **Interview Practice**: Help candidates prepare for interviews
3. **Skill Assessment**: Evaluate technical knowledge objectively
4. **Learning Tool**: Provide educational feedback

## 🔐 Security Notes

- Current implementation uses in-memory storage (demo purposes)
- For production: Implement proper database, authentication, and authorization
- Secure API endpoints with authentication tokens
- Add rate limiting and input validation

## 🚧 Future Enhancements

- [ ] Audio/video interview support
- [ ] User authentication system
- [ ] Interview history and analytics
- [ ] Custom question banks
- [ ] Multi-language support
- [ ] Real-time interview monitoring
- [ ] Integration with ATS systems

## 📝 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ using AI and Modern Web Technologies**
