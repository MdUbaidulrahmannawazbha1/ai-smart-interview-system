# Quick Start Guide

## 🚀 Execute the AI Smart Interview System

### One-Command Launch
```bash
./run.sh
```

This will start:
- ✅ Backend API Server (http://localhost:8000)
- ✅ Frontend Web Application (http://localhost:5173)

### Access Points

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:5173 | Main web interface |
| Backend API | http://localhost:8000 | REST API endpoints |
| API Docs (Swagger) | http://localhost:8000/docs | Interactive API documentation |
| API Docs (ReDoc) | http://localhost:8000/redoc | Alternative API documentation |
| Health Check | http://localhost:8000/api/v1/health/ | System health status |

### Individual Services

#### Backend Only
```bash
./start_backend.sh
```

#### Frontend Only
```bash
./start_frontend.sh
```

### Stop Services

Press `Ctrl+C` to stop all services when using `./run.sh`

### System Requirements

- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn

### First Time Setup

The scripts will automatically:
1. Create Python virtual environment (if needed)
2. Install Python dependencies
3. Install Node.js dependencies
4. Start the servers

No manual setup required! Just run `./run.sh`

---

For detailed information, see the main [README.md](README.md)
