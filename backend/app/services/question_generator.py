"""
Question generation service
"""
import random
import uuid
from typing import List
from app.schemas.interview import Question
from app.constants.messages import SAMPLE_QUESTIONS
from app.core.logger import logger


class QuestionGenerator:
    """Generate interview questions"""
    
    def __init__(self):
        self.question_bank = SAMPLE_QUESTIONS
    
    def generate_questions(
        self,
        position: str,
        num_questions: int = 5,
        categories: List[str] = None
    ) -> List[Question]:
        """
        Generate interview questions based on position
        
        Args:
            position: Job position
            num_questions: Number of questions to generate
            categories: Specific categories to include
            
        Returns:
            List of questions
        """
        logger.info(f"Generating {num_questions} questions for position: {position}")
        
        # Determine which question sets to use based on position
        position_lower = position.lower()
        available_questions = []
        
        # Add relevant questions based on position
        if "python" in position_lower or "backend" in position_lower:
            available_questions.extend(self.question_bank.get("python", []))
        
        if "javascript" in position_lower or "frontend" in position_lower or "fullstack" in position_lower:
            available_questions.extend(self.question_bank.get("javascript", []))
        
        # Always add some general questions
        available_questions.extend(self.question_bank.get("general", []))
        
        # If no specific questions found, use all available
        if not available_questions:
            for questions in self.question_bank.values():
                available_questions.extend(questions)
        
        # Filter by categories if specified
        if categories:
            available_questions = [
                q for q in available_questions
                if q.get("category") in categories
            ]
        
        # Randomly select questions
        num_to_select = min(num_questions, len(available_questions))
        selected_questions = random.sample(available_questions, num_to_select)
        
        # Convert to Question objects with unique IDs
        questions = []
        for q_data in selected_questions:
            question = Question(
                id=str(uuid.uuid4()),
                text=q_data["text"],
                category=q_data.get("category", "general"),
                difficulty=q_data.get("difficulty", "medium"),
                expected_keywords=q_data.get("expected_keywords", [])
            )
            questions.append(question)
        
        logger.info(f"Generated {len(questions)} questions")
        return questions
    
    def get_question_by_id(self, question_id: str, questions: List[Question]) -> Question:
        """
        Get a specific question by ID
        
        Args:
            question_id: Question ID
            questions: List of questions to search
            
        Returns:
            Question object or None
        """
        for question in questions:
            if question.id == question_id:
                return question
        return None


# Global question generator instance
question_generator = QuestionGenerator()
