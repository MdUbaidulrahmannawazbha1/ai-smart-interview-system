"""
Feedback schemas
"""
from pydantic import BaseModel
from typing import List, Optional


class DetailedFeedback(BaseModel):
    """Detailed feedback for an answer"""
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]
    key_points_covered: List[str]
    key_points_missed: List[str]


class FeedbackRequest(BaseModel):
    """Request for detailed feedback"""
    question_text: str
    answer_text: str
    expected_keywords: List[str] = []


class FeedbackResponse(BaseModel):
    """Response with detailed feedback"""
    feedback: DetailedFeedback
    message: str = "Feedback generated successfully"
