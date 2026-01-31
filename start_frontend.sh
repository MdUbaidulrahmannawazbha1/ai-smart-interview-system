#!/bin/bash

# Start Frontend Script for AI Smart Interview System
# This script sets up and runs the React frontend application

set -e

echo "🚀 Starting AI Smart Interview System - Frontend"
echo "================================================="

# Navigate to frontend directory
cd "$(dirname "$0")/frontend"

# Check if node_modules exists, if not install dependencies
if [ ! -d "node_modules" ]; then
    echo "📦 Installing npm dependencies..."
    npm install
fi

# Start the development server
echo "✨ Starting React development server..."
echo "🌐 Application will be available at: http://localhost:5173 or http://localhost:3000"
echo ""

npm run dev
