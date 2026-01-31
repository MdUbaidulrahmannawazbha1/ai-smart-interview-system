"""
evaluation.py

Pydantic schemas for evaluation-related data in AI-Powered Smart Interview System.
Defines data models for answer evaluation and scoring.
"""

from pydantic import BaseModel, Field
from typing import Optional


class EvaluationMetrics(BaseModel):
    """
    Schema for detailed evaluation metrics.
    """
    similarity_score: float = Field(..., description="Cosine similarity score (0-1)", ge=0.0, le=1.0)
    similarity_percentage: float = Field(..., description="Similarity as percentage (0-100)", ge=0.0, le=100.0)
    sentiment_label: str = Field(..., description="Sentiment classification: positive, neutral, or negative")
    sentiment_confidence: float = Field(..., description="Sentiment confidence score (0-1)", ge=0.0, le=1.0)


class ScoreBreakdown(BaseModel):
    """
    Schema for score breakdown showing component contributions.
    """
    content_score: float = Field(..., description="Score from content similarity (0-100)")
    sentiment_score: float = Field(..., description="Score from sentiment analysis (0-100)")
    final_score: float = Field(..., description="Weighted final score (0-100)")
    content_weight: float = Field(default=0.7, description="Weight given to content similarity")
    sentiment_weight: float = Field(default=0.3, description="Weight given to sentiment")


class DetailedEvaluation(BaseModel):
    """
    Schema for comprehensive evaluation results.
    """
    question: str = Field(..., description="The interview question")
    user_answer: str = Field(..., description="Candidate's answer")
    expected_answer: str = Field(..., description="Reference/expected answer")
    metrics: EvaluationMetrics = Field(..., description="Evaluation metrics")
    score_breakdown: ScoreBreakdown = Field(..., description="Detailed score breakdown")
    feedback: str = Field(..., description="Textual feedback on performance")
    recommendations: Optional[str] = Field(None, description="Improvement recommendations")


class BatchEvaluationResult(BaseModel):
    """
    Schema for batch evaluation of multiple answers.
    """
    total_questions: int = Field(..., description="Total number of questions evaluated")
    average_score: float = Field(..., description="Average score across all questions")
    highest_score: float = Field(..., description="Highest individual score")
    lowest_score: float = Field(..., description="Lowest individual score")
    overall_performance: str = Field(..., description="Overall performance assessment")
