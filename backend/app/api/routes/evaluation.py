"""
Evaluation endpoints
"""
from fastapi import APIRouter, HTTPException
from typing import Dict, List

from app.schemas.evaluation import (
    EvaluationRequest,
    EvaluationResponse,
    FinalEvaluationRequest,
    FinalEvaluationResponse,
    QuestionEvaluation
)
from app.services import answer_evaluator, scoring_engine, question_generator
from app.api.routes.interview import interview_sessions
from app.core.logger import logger

router = APIRouter()

# In-memory storage for evaluations
evaluations_store: Dict[str, List[QuestionEvaluation]] = {}


@router.post("/evaluate", response_model=EvaluationResponse)
async def evaluate_answer(request: EvaluationRequest):
    """
    Evaluate a single answer
    
    Args:
        request: Evaluation request
        
    Returns:
        Evaluation result
    """
    try:
        logger.info(f"Evaluating answer for session: {request.session_id}")
        
        # Get session to retrieve question details
        if request.session_id not in interview_sessions:
            raise HTTPException(status_code=404, detail="Session not found")
        
        session = interview_sessions[request.session_id]
        
        # Find the question
        question = None
        for q in session.questions:
            if q.id == request.question_id:
                question = q
                break
        
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        # Evaluate the answer
        evaluation = answer_evaluator.evaluate_answer(
            question_id=request.question_id,
            question_text=question.text,
            answer_text=request.answer_text,
            expected_keywords=question.expected_keywords
        )
        
        # Store evaluation
        if request.session_id not in evaluations_store:
            evaluations_store[request.session_id] = []
        evaluations_store[request.session_id].append(evaluation)
        
        logger.info(f"Evaluation completed: Score={evaluation.overall_score:.2f}")
        
        return EvaluationResponse(
            evaluation=evaluation,
            message="Answer evaluated successfully"
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error evaluating answer: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/final-evaluation", response_model=FinalEvaluationResponse)
async def get_final_evaluation(request: FinalEvaluationRequest):
    """
    Get final interview evaluation
    
    Args:
        request: Final evaluation request
        
    Returns:
        Complete evaluation with recommendations
    """
    try:
        logger.info(f"Generating final evaluation for session: {request.session_id}")
        
        # Check if session exists
        if request.session_id not in interview_sessions:
            raise HTTPException(status_code=404, detail="Session not found")
        
        # Get evaluations for this session
        evaluations = evaluations_store.get(request.session_id, [])
        
        # Calculate final evaluation
        final_eval = scoring_engine.calculate_final_evaluation(
            session_id=request.session_id,
            evaluations=evaluations
        )
        
        logger.info(f"Final evaluation completed: Average={final_eval.average_score:.2f}")
        
        return final_eval
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating final evaluation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/session/{session_id}/evaluations")
async def get_session_evaluations(session_id: str):
    """
    Get all evaluations for a session
    
    Args:
        session_id: Session identifier
        
    Returns:
        List of evaluations
    """
    try:
        if session_id not in interview_sessions:
            raise HTTPException(status_code=404, detail="Session not found")
        
        evaluations = evaluations_store.get(session_id, [])
        
        return {
            "status": "success",
            "session_id": session_id,
            "evaluations": [eval.dict() for eval in evaluations],
            "count": len(evaluations)
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting evaluations: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
