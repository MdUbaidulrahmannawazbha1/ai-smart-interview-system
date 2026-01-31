# Architecture

## Overview

The AI Smart Interview System is built using a modern microservices architecture with a clear separation between frontend and backend.

## System Components

### Backend (FastAPI)
- **API Layer**: RESTful API endpoints for interview management and evaluation
- **Services Layer**: Business logic for question generation, answer evaluation, sentiment analysis
- **ML Layer**: Machine learning models for NLP tasks (TF-IDF, sentiment analysis)
- **Utilities**: Helper functions for text processing, audio handling, and response formatting

### Frontend (React)
- **User Interface**: Interactive interview interface
- **State Management**: React hooks for managing application state
- **API Integration**: Axios for backend communication

## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **ML/NLP**: 
  - Transformers (Hugging Face) for sentiment analysis
  - scikit-learn for TF-IDF vectorization and cosine similarity
  - SpeechRecognition for audio transcription
- **Configuration**: Pydantic for settings management

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **HTTP Client**: Axios

## Data Flow

1. **Interview Start**: User provides details → Backend generates questions
2. **Answer Submission**: User answers → Backend processes and stores
3. **Evaluation**: Answer text → ML models analyze → Scoring engine computes grades
4. **Results**: Final evaluation → Recommendations generated → Displayed to user

## ML Models

### Sentiment Analysis
- Model: DistilBERT (fine-tuned for sentiment)
- Purpose: Analyze confidence and tone in answers

### Text Similarity
- Method: TF-IDF + Cosine Similarity
- Purpose: Measure semantic similarity between questions and answers

### Keyword Matching
- Method: Custom keyword extraction and matching
- Purpose: Verify coverage of expected technical terms

## Scoring Algorithm

Overall Score = 
- 40% Semantic Similarity (TF-IDF + Cosine)
- 40% Keyword Match
- 20% Sentiment Score

Grades:
- Excellent: ≥80%
- Good: ≥60%
- Average: ≥40%
- Poor: <40%
