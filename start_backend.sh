#!/bin/bash

# Start Backend Script for AI Smart Interview System
# This script sets up and runs the FastAPI backend server

set -e

echo "🚀 Starting AI Smart Interview System - Backend"
echo "================================================"

# Navigate to backend directory
cd "$(dirname "$0")/backend"

# Check if virtual environment exists, if not create it
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo "📝 Creating .env file from .env.example..."
        cp .env.example .env
    fi
fi

# Start the FastAPI server
echo "✨ Starting FastAPI server..."
echo "📚 API Documentation will be available at: http://localhost:8000/docs"
echo "🔍 Alternative docs at: http://localhost:8000/redoc"
echo ""

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
