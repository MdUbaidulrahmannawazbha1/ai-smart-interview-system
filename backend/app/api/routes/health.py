"""
health.py

Health check API router for AI-Powered Smart Interview System. 
Provides endpoints for monitoring service availability and status.
"""

from fastapi import APIRouter

# Initialize router with tags for API documentation
router = APIRouter(
    prefix="/health",
    tags=["Health Check"],
)


@router.get("/")
async def health_check():
    """
    Health check endpoint for monitoring service availability.
    
    Returns:
        dict: Service health status and identification
    """
    return {
        "status": "healthy",
        "service": "AI-Powered Smart Interview System",
    }
