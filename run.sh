#!/bin/bash

# Main Execution Script for AI Smart Interview System
# This script starts both backend and frontend services

set -e

echo "🚀 AI Smart Interview System - Full Stack Launcher"
echo "===================================================="
echo ""
echo "This script will start both backend and frontend services."
echo "Press Ctrl+C to stop both services."
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Function to cleanup background processes on exit
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill 0
    exit 0
}

# Set trap to catch SIGINT (Ctrl+C) and SIGTERM
trap cleanup SIGINT SIGTERM

# Start backend in background
echo "🔧 Starting Backend Server..."
"$SCRIPT_DIR/start_backend.sh" &
BACKEND_PID=$!

# Wait a bit for backend to initialize
sleep 5

# Start frontend in background
echo "🎨 Starting Frontend Application..."
"$SCRIPT_DIR/start_frontend.sh" &
FRONTEND_PID=$!

echo ""
echo "✅ Both services are starting up!"
echo "=================================================="
echo "📡 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo "🌐 Frontend: http://localhost:5173 or http://localhost:3000"
echo "=================================================="
echo "Press Ctrl+C to stop all services"
echo ""

# Wait for both processes
wait
