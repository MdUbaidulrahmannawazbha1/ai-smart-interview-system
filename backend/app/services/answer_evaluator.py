"""
Answer evaluation service
"""
from typing import List
from app.ml import TFIDFVectorizer, cosine_similarity
from app.utils import calculate_keyword_match_score, clean_text
from app.services.sentiment_analyzer import sentiment_analyzer
from app.schemas.evaluation import QuestionEvaluation
from app.core.config import settings
from app.core.logger import logger


class AnswerEvaluator:
    """Evaluate interview answers"""
    
    def __init__(self):
        self.vectorizer = TFIDFVectorizer()
    
    def evaluate_answer(
        self,
        question_id: str,
        question_text: str,
        answer_text: str,
        expected_keywords: List[str] = None
    ) -> QuestionEvaluation:
        """
        Evaluate an answer to a question
        
        Args:
            question_id: Question identifier
            question_text: The question text
            answer_text: The answer text
            expected_keywords: Optional list of expected keywords
            
        Returns:
            QuestionEvaluation object
        """
        logger.info(f"Evaluating answer for question: {question_id}")
        
        # Clean texts
        clean_question = clean_text(question_text)
        clean_answer = clean_text(answer_text)
        
        # Calculate similarity score using TF-IDF and cosine similarity
        similarity_score = self._calculate_similarity(clean_question, clean_answer)
        
        # Calculate keyword match score
        keyword_match_score = 0.0
        if expected_keywords:
            keyword_match_score = calculate_keyword_match_score(
                clean_answer,
                expected_keywords
            )
        else:
            # If no keywords provided, use a neutral score
            keyword_match_score = 0.5
        
        # Get sentiment score
        sentiment_score = sentiment_analyzer.get_sentiment_score(clean_answer)
        
        # Calculate overall score (weighted average)
        overall_score = (
            similarity_score * 0.4 +
            keyword_match_score * 0.4 +
            sentiment_score * 0.2
        )
        
        # Determine grade
        grade = self._determine_grade(overall_score)
        
        # Generate feedback
        feedback = self._generate_feedback(
            similarity_score,
            keyword_match_score,
            sentiment_score,
            overall_score,
            grade
        )
        
        logger.info(f"Evaluation complete: Score={overall_score:.2f}, Grade={grade}")
        
        return QuestionEvaluation(
            question_id=question_id,
            question_text=question_text,
            answer_text=answer_text,
            similarity_score=round(similarity_score, 3),
            sentiment_score=round(sentiment_score, 3),
            keyword_match_score=round(keyword_match_score, 3),
            overall_score=round(overall_score, 3),
            feedback=feedback,
            grade=grade
        )
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate semantic similarity between two texts"""
        try:
            # Create TF-IDF vectors
            vectors = self.vectorizer.fit_transform([text1, text2])
            
            # Calculate cosine similarity
            similarity = cosine_similarity(vectors[0], vectors[1])
            
            return max(0.0, min(1.0, similarity))
        except Exception as e:
            logger.error(f"Error calculating similarity: {str(e)}")
            return 0.0
    
    def _determine_grade(self, score: float) -> str:
        """Determine grade based on score"""
        if score >= settings.EXCELLENT_THRESHOLD:
            return "excellent"
        elif score >= settings.GOOD_THRESHOLD:
            return "good"
        elif score >= settings.AVERAGE_THRESHOLD:
            return "average"
        else:
            return "poor"
    
    def _generate_feedback(
        self,
        similarity_score: float,
        keyword_score: float,
        sentiment_score: float,
        overall_score: float,
        grade: str
    ) -> str:
        """Generate feedback based on scores"""
        feedback_parts = []
        
        # Overall assessment
        if grade == "excellent":
            feedback_parts.append("Excellent answer! You demonstrated comprehensive understanding.")
        elif grade == "good":
            feedback_parts.append("Good answer with solid understanding of the topic.")
        elif grade == "average":
            feedback_parts.append("Average answer. There's room for improvement.")
        else:
            feedback_parts.append("The answer needs significant improvement.")
        
        # Specific feedback
        if similarity_score < 0.4:
            feedback_parts.append("Try to address the question more directly.")
        
        if keyword_score < 0.4:
            feedback_parts.append("Consider including more relevant technical terms and concepts.")
        
        if sentiment_score < 0.4:
            feedback_parts.append("Try to present your answer with more confidence and clarity.")
        
        if similarity_score >= 0.7 and keyword_score >= 0.6:
            feedback_parts.append("You covered the key points well.")
        
        return " ".join(feedback_parts)


# Global answer evaluator instance
answer_evaluator = AnswerEvaluator()
