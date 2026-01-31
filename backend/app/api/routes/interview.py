"""
Interview endpoints
"""
from fastapi import APIRouter, HTTPException
from typing import Dict
import uuid
from datetime import datetime

from app.schemas.interview import (
    InterviewRequest,
    InterviewResponse,
    InterviewSession,
    Answer
)
from app.services import question_generator
from app.core.logger import logger

router = APIRouter()

# In-memory storage for demo (in production, use a database)
interview_sessions: Dict[str, InterviewSession] = {}


@router.post("/start", response_model=InterviewResponse)
async def start_interview(request: InterviewRequest):
    """
    Start a new interview session
    
    Args:
        request: Interview request with candidate details
        
    Returns:
        Interview session with questions
    """
    try:
        logger.info(f"Starting interview for {request.candidate_name}")
        
        # Generate session ID
        session_id = str(uuid.uuid4())
        
        # Generate questions
        questions = question_generator.generate_questions(
            position=request.position,
            num_questions=request.num_questions
        )
        
        # Create interview session
        session = InterviewSession(
            session_id=session_id,
            candidate_name=request.candidate_name,
            position=request.position,
            questions=questions,
            start_time=datetime.now(),
            status="in_progress"
        )
        
        # Store session
        interview_sessions[session_id] = session
        
        logger.info(f"Interview session created: {session_id}")
        
        return InterviewResponse(
            session_id=session_id,
            questions=questions,
            message="Interview session created successfully"
        )
    
    except Exception as e:
        logger.error(f"Error starting interview: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/submit-answer")
async def submit_answer(answer: Answer):
    """
    Submit an answer to a question
    
    Args:
        answer: Answer data
        
    Returns:
        Success message
    """
    try:
        logger.info(f"Answer submitted for question: {answer.question_id}")
        
        # Note: In a real application, you would:
        # 1. Validate the session exists
        # 2. Store the answer
        # 3. Potentially trigger evaluation
        
        return {
            "status": "success",
            "message": "Answer submitted successfully",
            "question_id": answer.question_id
        }
    
    except Exception as e:
        logger.error(f"Error submitting answer: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/session/{session_id}")
async def get_session(session_id: str):
    """
    Get interview session details
    
    Args:
        session_id: Session identifier
        
    Returns:
        Interview session data
    """
    try:
        if session_id not in interview_sessions:
            raise HTTPException(status_code=404, detail="Session not found")
        
        session = interview_sessions[session_id]
        
        return {
            "status": "success",
            "session": session.dict()
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting session: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/end/{session_id}")
async def end_interview(session_id: str):
    """
    End an interview session
    
    Args:
        session_id: Session identifier
        
    Returns:
        Success message
    """
    try:
        if session_id not in interview_sessions:
            raise HTTPException(status_code=404, detail="Session not found")
        
        session = interview_sessions[session_id]
        session.status = "completed"
        session.end_time = datetime.now()
        
        logger.info(f"Interview session ended: {session_id}")
        
        return {
            "status": "success",
            "message": "Interview session ended successfully",
            "session_id": session_id
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error ending interview: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
