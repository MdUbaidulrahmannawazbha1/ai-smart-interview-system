"""
evaluation.py

Answer evaluation API router for AI-Powered Smart Interview System. 
Handles HTTP requests and orchestrates answer evaluation using ML and service layers.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.ml.tfidf_vectorizer import vectorize_texts
from app. ml.cosine_similarity import compute_cosine_similarity
from app.services.sentiment_analyzer import analyze_sentiment
from app.services. scoring_engine import calculate_final_score


class EvaluationRequest(BaseModel):
    """
    Schema for answer evaluation request.
    """
    question: str = Field(..., description="Interview question that was asked")
    user_answer: str = Field(..., description="Candidate's answer to the question")
    expected_answer: str = Field(..., description="Reference or expected answer")


class SentimentResult(BaseModel):
    """
    Schema for sentiment analysis result. 
    """
    label: str = Field(..., description="Sentiment label (positive/neutral/negative)")
    confidence: float = Field(..., description="Confidence score (0-1)")


class EvaluationResponse(BaseModel):
    """
    Schema for answer evaluation response.
    """
    similarity_percentage: float = Field(..., description="Similarity score as percentage (0-100)")
    sentiment: SentimentResult = Field(..., description="Sentiment analysis results")
    final_score: float = Field(..., description="Final interview score (0-100)")
    overall_feedback: str = Field(... , description="Overall performance feedback")


router = APIRouter(
    prefix="/interview",
    tags=["Interview"],
)


@router.post("/evaluate", response_model=EvaluationResponse)
async def evaluate_interview_answer(request: EvaluationRequest):
    """
    Evaluate a candidate's answer using ML-based analysis.
    
    Performs TF-IDF vectorization, cosine similarity computation,
    sentiment analysis, and final score calculation. 
    
    Args:
        request:  EvaluationRequest containing question and answers
        
    Returns:
        EvaluationResponse:  Comprehensive evaluation results
        
    Raises:
        HTTPException: If evaluation fails at any stage
    """
    try:
        # Step 1: Vectorize answers using TF-IDF
        user_vector, expected_vector = vectorize_texts(
            request.user_answer,
            request.expected_answer
        )
        
        # Step 2: Compute cosine similarity
        similarity_score = compute_cosine_similarity(user_vector, expected_vector)
        
        # Step 3: Convert similarity to percentage
        similarity_percentage = similarity_score * 100
        
        # Step 4: Analyze sentiment of user's answer
        sentiment_result = analyze_sentiment(request.user_answer)
        
        # Step 5: Calculate final score
        final_result = calculate_final_score(
            similarity_percentage=similarity_percentage,
            sentiment_label=sentiment_result["sentiment"],
            sentiment_confidence=sentiment_result["confidence"]
        )
        
        # Step 6: Construct and return response
        return EvaluationResponse(
            similarity_percentage=round(similarity_percentage, 2),
            sentiment=SentimentResult(
                label=sentiment_result["sentiment"],
                confidence=sentiment_result["confidence"]
            ),
            final_score=final_result["final_score"],
            overall_feedback=final_result["overall_feedback"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Answer evaluation failed: {str(e)}"
        )