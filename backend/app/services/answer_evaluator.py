"""
answer_evaluator.py

Service layer for comprehensive answer evaluation in AI-Powered Smart Interview System.
Orchestrates multiple evaluation techniques to assess candidate responses.
"""

from typing import Dict, Any
from app.ml.tfidf_vectorizer import vectorize_texts
from app.ml.cosine_similarity import compute_cosine_similarity
from app.services.sentiment_analyzer import analyze_sentiment
from app.services.scoring_engine import calculate_final_score


def evaluate_answer(
    question: str,
    user_answer: str,
    expected_answer: str
) -> Dict[str, Any]:
    """
    Comprehensively evaluate a candidate's answer.
    
    Combines multiple evaluation techniques:
    - Semantic similarity using TF-IDF and cosine similarity
    - Sentiment analysis of the response
    - Final score calculation with weighted components
    
    Args:
        question: The interview question that was asked
        user_answer: The candidate's answer
        expected_answer: Reference or expected answer
        
    Returns:
        dict: Complete evaluation results including scores and feedback
        
    Raises:
        Exception: If evaluation fails at any stage
    """
    try:
        # Step 1: Vectorize answers using TF-IDF
        user_vector, expected_vector = vectorize_texts(
            user_answer,
            expected_answer
        )
        
        # Step 2: Compute semantic similarity
        similarity_score = compute_cosine_similarity(user_vector, expected_vector)
        similarity_percentage = similarity_score * 100
        
        # Step 3: Analyze sentiment of the answer
        sentiment_result = analyze_sentiment(user_answer)
        
        # Step 4: Calculate final score with weighted components
        final_result = calculate_final_score(
            similarity_percentage=similarity_percentage,
            sentiment_label=sentiment_result["sentiment"],
            sentiment_confidence=sentiment_result["confidence"]
        )
        
        # Step 5: Compile comprehensive evaluation
        evaluation = {
            "similarity_score": round(similarity_score, 4),
            "similarity_percentage": round(similarity_percentage, 2),
            "sentiment": sentiment_result["sentiment"],
            "sentiment_confidence": sentiment_result["confidence"],
            "final_score": final_result["final_score"],
            "overall_feedback": final_result["overall_feedback"],
            "question": question,
        }
        
        return evaluation
        
    except Exception as e:
        raise Exception(f"Answer evaluation failed: {str(e)}")


def evaluate_multiple_answers(
    qa_pairs: list
) -> Dict[str, Any]:
    """
    Evaluate multiple question-answer pairs in batch.
    
    Args:
        qa_pairs: List of dicts with 'question', 'user_answer', 'expected_answer'
        
    Returns:
        dict: Aggregated evaluation results for all answers
    """
    if not qa_pairs:
        return {
            "average_score": 0.0,
            "evaluations": [],
            "total_questions": 0,
        }
    
    evaluations = []
    total_score = 0.0
    
    for qa in qa_pairs:
        try:
            eval_result = evaluate_answer(
                question=qa.get("question", ""),
                user_answer=qa.get("user_answer", ""),
                expected_answer=qa.get("expected_answer", "")
            )
            evaluations.append(eval_result)
            total_score += eval_result["final_score"]
        except Exception as e:
            evaluations.append({
                "error": str(e),
                "question": qa.get("question", ""),
            })
    
    return {
        "average_score": round(total_score / len(qa_pairs), 2),
        "evaluations": evaluations,
        "total_questions": len(qa_pairs),
    }
