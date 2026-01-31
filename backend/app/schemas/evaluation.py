"""
Evaluation schemas
"""
from pydantic import BaseModel
from typing import List, Optional


class QuestionEvaluation(BaseModel):
    """Evaluation for a single question"""
    question_id: str
    question_text: str
    answer_text: str
    similarity_score: float
    sentiment_score: float
    keyword_match_score: float
    overall_score: float
    feedback: str
    grade: str  # excellent, good, average, poor


class EvaluationRequest(BaseModel):
    """Request to evaluate an answer"""
    session_id: str
    question_id: str
    answer_text: str


class EvaluationResponse(BaseModel):
    """Response with evaluation results"""
    evaluation: QuestionEvaluation
    message: str = "Answer evaluated successfully"


class FinalEvaluationRequest(BaseModel):
    """Request for final interview evaluation"""
    session_id: str


class FinalEvaluationResponse(BaseModel):
    """Final interview evaluation"""
    session_id: str
    evaluations: List[QuestionEvaluation]
    average_score: float
    total_questions: int
    answered_questions: int
    overall_grade: str
    summary: str
    recommendations: List[str]
