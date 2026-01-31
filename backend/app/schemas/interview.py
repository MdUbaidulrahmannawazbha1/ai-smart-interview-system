"""
interview.py

Pydantic schemas for interview-related data in AI-Powered Smart Interview System.
Defines data models for interview requests and responses.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class InterviewSession(BaseModel):
    """
    Schema for an interview session.
    """
    session_id: str = Field(..., description="Unique session identifier")
    candidate_name: Optional[str] = Field(None, description="Name of the candidate")
    role: str = Field(..., description="Job role for the interview")
    difficulty: str = Field(..., description="Difficulty level: easy, medium, or hard")
    started_at: datetime = Field(default_factory=datetime.now, description="Session start time")
    status: str = Field(default="active", description="Session status: active, completed, or cancelled")


class QuestionRecord(BaseModel):
    """
    Schema for a single interview question record.
    """
    question_id: str = Field(..., description="Unique question identifier")
    question_text: str = Field(..., description="The interview question")
    asked_at: datetime = Field(default_factory=datetime.now, description="Time when question was asked")
    answer_text: Optional[str] = Field(None, description="Candidate's answer")
    answered_at: Optional[datetime] = Field(None, description="Time when answer was provided")


class InterviewProgress(BaseModel):
    """
    Schema for tracking interview progress.
    """
    session_id: str = Field(..., description="Session identifier")
    total_questions: int = Field(default=0, description="Total questions asked")
    answered_questions: int = Field(default=0, description="Questions answered")
    current_score: Optional[float] = Field(None, description="Current cumulative score")
    completion_percentage: float = Field(default=0.0, description="Progress percentage")


class InterviewSummary(BaseModel):
    """
    Schema for interview summary/results.
    """
    session_id: str = Field(..., description="Session identifier")
    candidate_name: Optional[str] = Field(None, description="Candidate name")
    role: str = Field(..., description="Job role")
    total_questions: int = Field(..., description="Total questions in interview")
    average_score: float = Field(..., description="Average score across all questions")
    overall_feedback: str = Field(..., description="Overall performance feedback")
    completed_at: datetime = Field(default_factory=datetime.now, description="Completion time")
