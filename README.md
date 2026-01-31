# AI Smart Interview System

AI Smart Interview System is an intelligent interview platform that leverages artificial intelligence to conduct, evaluate, and provide feedback on technical interviews. The system combines speech recognition, natural language processing, and machine learning to create an automated interview experience.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn

### Running the Project

#### Option 1: Run Both Backend and Frontend Together (Recommended)

```bash
./run.sh
```

This will start both the backend API server and the frontend application simultaneously.

#### Option 2: Run Backend Only

```bash
./start_backend.sh
```

The backend API will be available at:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

#### Option 3: Run Frontend Only

```bash
./start_frontend.sh
```

The frontend application will be available at:
- http://localhost:5173 or http://localhost:3000

### Manual Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (if needed)
cp .env.example .env

# Run the server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 📚 Features

- AI-powered interview question generation
- Real-time answer evaluation
- Speech-to-text processing
- Sentiment analysis
- Automated scoring engine
- RESTful API
- Interactive web interface

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Python**: Core programming language
- **scikit-learn**: Machine learning library
- **TextBlob**: NLP library for sentiment analysis
- **NumPy**: Numerical computing

### Frontend
- **React**: UI library
- **JavaScript/JSX**: Frontend development

## 📖 API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🏗️ Project Structure

```
ai-smart-interview-system/
├── backend/           # FastAPI backend application
│   ├── app/
│   │   ├── api/      # API routes
│   │   ├── core/     # Core configurations
│   │   ├── ml/       # Machine learning models
│   │   ├── services/ # Business logic services
│   │   ├── schemas/  # Pydantic schemas
│   │   └── utils/    # Utility functions
│   └── tests/        # Backend tests
├── frontend/         # React frontend application
│   └── src/
├── docs/             # Documentation
└── run.sh           # Main execution script
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.
