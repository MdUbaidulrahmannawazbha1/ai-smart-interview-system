"""
interview.py

Interview question generation API router for AI-Powered Smart Interview System.
Handles HTTP requests and delegates question generation to the service layer.
"""

from typing import List, Optional
from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.question_generator import generate_question


class QuestionRequest(BaseModel):
    """
    Schema for interview question generation request.
    """
    role: str = Field(..., description="Job role for the interview")
    difficulty: str = Field(..., description="Difficulty level: easy, medium, or hard")
    previous_questions: Optional[List[str]] = Field(
        default=None,
        description="Previously asked questions for context-aware generation",
    )


class QuestionResponse(BaseModel):
    """
    Schema for interview question response.
    """
    question: str
    role: str
    difficulty: str


router = APIRouter(
    prefix="/interview",
    tags=["Interview"],
)


@router.post("/question", response_model=QuestionResponse)
async def generate_interview_question(request: QuestionRequest):
    """
    Generate a single interview question based on role and difficulty.
    """
    question = generate_question(
        role=request.role,
        difficulty=request.difficulty,
        previous_questions=request.previous_questions,
    )

    return QuestionResponse(
        question=question,
        role=request.role,
        difficulty=request.difficulty,
    )
