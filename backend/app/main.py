"""
main.py

FastAPI application entry point for AI-Powered Smart Interview System.  
Initializes the FastAPI app, configures CORS, registers API routes,
and provides system health check endpoints.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.interview import router as interview_router
from app.api.routes.evaluation import router as evaluation_router


# Initialize FastAPI application
app = FastAPI(
    title="AI-Powered Smart Interview System",
    description="An intelligent system that simulates technical and HR interviews using AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(health_router, prefix="/api/v1")
app.include_router(interview_router, prefix="/api/v1")
app.include_router(evaluation_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    """
    Application startup event handler.
    Logs system initialization. 
    """
    print("🚀 AI-Powered Smart Interview System starting...")
    print("📚 API Documentation available at /docs")


@app.get("/")
async def root():
    """
    Root endpoint returning system status.
    
    Returns:
        dict: System status and service name
    """
    return {
        "status": "running",
        "service": "AI-Powered Smart Interview System",
    }