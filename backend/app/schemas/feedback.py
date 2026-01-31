"""
feedback.py

Pydantic schemas for feedback-related data in AI-Powered Smart Interview System.
Defines data models for providing feedback to candidates.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class FeedbackPoint(BaseModel):
    """
    Schema for a single feedback point.
    """
    category: str = Field(..., description="Feedback category: strength, weakness, or suggestion")
    message: str = Field(..., description="Feedback message")
    severity: Optional[str] = Field(None, description="Severity level: low, medium, high")


class QuestionFeedback(BaseModel):
    """
    Schema for feedback on a specific question.
    """
    question_id: str = Field(..., description="Question identifier")
    question_text: str = Field(..., description="The question text")
    score: float = Field(..., description="Score for this question (0-100)")
    feedback_points: List[FeedbackPoint] = Field(default_factory=list, description="List of feedback points")
    summary: str = Field(..., description="Summary feedback for this question")


class OverallFeedback(BaseModel):
    """
    Schema for overall interview feedback.
    """
    session_id: str = Field(..., description="Interview session identifier")
    candidate_name: Optional[str] = Field(None, description="Candidate name")
    overall_score: float = Field(..., description="Overall interview score (0-100)")
    performance_level: str = Field(..., description="Performance level: excellent, good, fair, poor")
    strengths: List[str] = Field(default_factory=list, description="List of identified strengths")
    areas_for_improvement: List[str] = Field(default_factory=list, description="Areas needing improvement")
    detailed_feedback: List[QuestionFeedback] = Field(default_factory=list, description="Per-question feedback")
    recommendations: str = Field(..., description="Personalized recommendations")
    generated_at: datetime = Field(default_factory=datetime.now, description="Feedback generation time")


class FeedbackSummary(BaseModel):
    """
    Schema for a brief feedback summary.
    """
    score: float = Field(..., description="Numeric score (0-100)")
    grade: str = Field(..., description="Letter grade or rating")
    message: str = Field(..., description="Brief feedback message")
    next_steps: Optional[str] = Field(None, description="Suggested next steps")
