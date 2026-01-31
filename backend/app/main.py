"""
FastAPI main application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logger import logger
from app.api.routes import health, interview, evaluation

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["Health"])
app.include_router(
    interview.router,
    prefix=f"{settings.API_V1_PREFIX}/interview",
    tags=["Interview"]
)
app.include_router(
    evaluation.router,
    prefix=f"{settings.API_V1_PREFIX}/evaluation",
    tags=["Evaluation"]
)


@app.on_event("startup")
async def startup_event():
    """Startup event handler"""
    logger.info(f"Starting {settings.PROJECT_NAME} v{settings.VERSION}")
    logger.info("Loading ML models...")
    
    try:
        # Pre-load models to avoid cold start
        from app.ml.model_loader import model_loader
        model_loader.load_sentiment_model()
        logger.info("ML models loaded successfully")
    except Exception as e:
        logger.warning(f"Could not pre-load ML models: {str(e)}")
        logger.warning("Models will be loaded on first use")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler"""
    logger.info(f"Shutting down {settings.PROJECT_NAME}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
