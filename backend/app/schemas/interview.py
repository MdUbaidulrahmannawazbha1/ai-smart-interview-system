"""
Interview schemas
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Question(BaseModel):
    """Interview question schema"""
    id: str
    text: str
    category: str = "general"
    difficulty: str = "medium"
    expected_keywords: List[str] = []


class Answer(BaseModel):
    """Interview answer schema"""
    question_id: str
    text: str
    audio_url: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)


class InterviewSession(BaseModel):
    """Interview session schema"""
    session_id: str
    candidate_name: str
    position: str
    questions: List[Question]
    answers: List[Answer] = []
    start_time: datetime = Field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    status: str = "in_progress"  # in_progress, completed, cancelled


class InterviewRequest(BaseModel):
    """Request to start an interview"""
    candidate_name: str
    position: str
    num_questions: int = 5


class InterviewResponse(BaseModel):
    """Response with interview session details"""
    session_id: str
    questions: List[Question]
    message: str = "Interview session created successfully"
