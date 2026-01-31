"""
Scoring engine for overall interview evaluation
"""
from typing import List
from app.schemas.evaluation import QuestionEvaluation, FinalEvaluationResponse
from app.core.logger import logger


class ScoringEngine:
    """Calculate overall interview scores and generate summaries"""
    
    def calculate_final_evaluation(
        self,
        session_id: str,
        evaluations: List[QuestionEvaluation]
    ) -> FinalEvaluationResponse:
        """
        Calculate final interview evaluation
        
        Args:
            session_id: Interview session ID
            evaluations: List of question evaluations
            
        Returns:
            Final evaluation response
        """
        logger.info(f"Calculating final evaluation for session: {session_id}")
        
        if not evaluations:
            return FinalEvaluationResponse(
                session_id=session_id,
                evaluations=[],
                average_score=0.0,
                total_questions=0,
                answered_questions=0,
                overall_grade="poor",
                summary="No answers were provided.",
                recommendations=["Please attempt all questions in future interviews."]
            )
        
        # Calculate average score
        total_score = sum(eval.overall_score for eval in evaluations)
        average_score = total_score / len(evaluations)
        
        # Determine overall grade
        overall_grade = self._determine_overall_grade(average_score)
        
        # Generate summary
        summary = self._generate_summary(evaluations, average_score, overall_grade)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(evaluations, average_score)
        
        logger.info(f"Final evaluation: Score={average_score:.2f}, Grade={overall_grade}")
        
        return FinalEvaluationResponse(
            session_id=session_id,
            evaluations=evaluations,
            average_score=round(average_score, 3),
            total_questions=len(evaluations),
            answered_questions=len(evaluations),
            overall_grade=overall_grade,
            summary=summary,
            recommendations=recommendations
        )
    
    def _determine_overall_grade(self, average_score: float) -> str:
        """Determine overall grade from average score"""
        if average_score >= 0.8:
            return "excellent"
        elif average_score >= 0.6:
            return "good"
        elif average_score >= 0.4:
            return "average"
        else:
            return "poor"
    
    def _generate_summary(
        self,
        evaluations: List[QuestionEvaluation],
        average_score: float,
        overall_grade: str
    ) -> str:
        """Generate interview summary"""
        total = len(evaluations)
        excellent_count = sum(1 for e in evaluations if e.grade == "excellent")
        good_count = sum(1 for e in evaluations if e.grade == "good")
        average_count = sum(1 for e in evaluations if e.grade == "average")
        poor_count = sum(1 for e in evaluations if e.grade == "poor")
        
        summary_parts = [
            f"Interview Performance: {overall_grade.capitalize()}",
            f"Average Score: {average_score:.1%}",
            f"Questions Answered: {total}",
            f"Grade Distribution: {excellent_count} Excellent, {good_count} Good, {average_count} Average, {poor_count} Poor"
        ]
        
        if overall_grade == "excellent":
            summary_parts.append("Outstanding performance! You demonstrated strong knowledge and communication skills.")
        elif overall_grade == "good":
            summary_parts.append("Good performance overall with solid understanding of the topics.")
        elif overall_grade == "average":
            summary_parts.append("Average performance. Some areas need improvement.")
        else:
            summary_parts.append("Performance needs significant improvement.")
        
        return ". ".join(summary_parts) + "."
    
    def _generate_recommendations(
        self,
        evaluations: List[QuestionEvaluation],
        average_score: float
    ) -> List[str]:
        """Generate improvement recommendations"""
        recommendations = []
        
        # Analyze weak areas
        low_similarity_count = sum(1 for e in evaluations if e.similarity_score < 0.5)
        low_keyword_count = sum(1 for e in evaluations if e.keyword_match_score < 0.5)
        low_sentiment_count = sum(1 for e in evaluations if e.sentiment_score < 0.5)
        
        if low_similarity_count > len(evaluations) * 0.3:
            recommendations.append(
                "Focus on understanding the question thoroughly before answering."
            )
        
        if low_keyword_count > len(evaluations) * 0.3:
            recommendations.append(
                "Study technical concepts and terminology more deeply."
            )
        
        if low_sentiment_count > len(evaluations) * 0.3:
            recommendations.append(
                "Work on presenting your answers with more confidence and clarity."
            )
        
        if average_score >= 0.7:
            recommendations.append("Keep up the excellent work!")
            recommendations.append("Consider mentoring others or preparing for advanced roles.")
        elif average_score >= 0.5:
            recommendations.append("Review fundamental concepts in your weak areas.")
            recommendations.append("Practice explaining technical topics clearly.")
        else:
            recommendations.append("Dedicate more time to studying core concepts.")
            recommendations.append("Practice mock interviews to improve communication.")
            recommendations.append("Seek feedback from experienced professionals.")
        
        return recommendations


# Global scoring engine instance
scoring_engine = ScoringEngine()
