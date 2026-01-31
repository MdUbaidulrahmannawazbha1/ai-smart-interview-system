"""
Application constants and messages
"""

# Success Messages
SUCCESS_INTERVIEW_CREATED = "Interview session created successfully"
SUCCESS_ANSWER_SUBMITTED = "Answer submitted successfully"
SUCCESS_EVALUATION_COMPLETED = "Evaluation completed successfully"

# Error Messages
ERROR_SESSION_NOT_FOUND = "Interview session not found"
ERROR_QUESTION_NOT_FOUND = "Question not found"
ERROR_INVALID_INPUT = "Invalid input provided"
ERROR_PROCESSING_FAILED = "Processing failed"
ERROR_MODEL_LOADING_FAILED = "Failed to load ML model"

# Grades
GRADE_EXCELLENT = "excellent"
GRADE_GOOD = "good"
GRADE_AVERAGE = "average"
GRADE_POOR = "poor"

# Question Categories
CATEGORY_TECHNICAL = "technical"
CATEGORY_BEHAVIORAL = "behavioral"
CATEGORY_SITUATIONAL = "situational"
CATEGORY_GENERAL = "general"

# Difficulty Levels
DIFFICULTY_EASY = "easy"
DIFFICULTY_MEDIUM = "medium"
DIFFICULTY_HARD = "hard"

# Sample Questions Bank
SAMPLE_QUESTIONS = {
    "python": [
        {
            "text": "Explain the difference between list and tuple in Python.",
            "category": CATEGORY_TECHNICAL,
            "difficulty": DIFFICULTY_EASY,
            "expected_keywords": ["immutable", "mutable", "list", "tuple", "ordered", "performance"]
        },
        {
            "text": "What are Python decorators and how do they work?",
            "category": CATEGORY_TECHNICAL,
            "difficulty": DIFFICULTY_MEDIUM,
            "expected_keywords": ["decorator", "function", "wrapper", "syntactic sugar", "higher-order"]
        },
        {
            "text": "Explain the Global Interpreter Lock (GIL) in Python.",
            "category": CATEGORY_TECHNICAL,
            "difficulty": DIFFICULTY_HARD,
            "expected_keywords": ["GIL", "threading", "multiprocessing", "lock", "concurrency", "CPython"]
        }
    ],
    "javascript": [
        {
            "text": "What is the difference between var, let, and const in JavaScript?",
            "category": CATEGORY_TECHNICAL,
            "difficulty": DIFFICULTY_EASY,
            "expected_keywords": ["scope", "hoisting", "var", "let", "const", "block"]
        },
        {
            "text": "Explain closures in JavaScript with an example.",
            "category": CATEGORY_TECHNICAL,
            "difficulty": DIFFICULTY_MEDIUM,
            "expected_keywords": ["closure", "scope", "function", "lexical", "encapsulation"]
        }
    ],
    "general": [
        {
            "text": "Tell me about yourself and your background.",
            "category": CATEGORY_GENERAL,
            "difficulty": DIFFICULTY_EASY,
            "expected_keywords": ["experience", "skills", "background", "education"]
        },
        {
            "text": "Describe a challenging project you worked on and how you overcame obstacles.",
            "category": CATEGORY_BEHAVIORAL,
            "difficulty": DIFFICULTY_MEDIUM,
            "expected_keywords": ["challenge", "solution", "teamwork", "problem-solving", "result"]
        },
        {
            "text": "Where do you see yourself in 5 years?",
            "category": CATEGORY_BEHAVIORAL,
            "difficulty": DIFFICULTY_EASY,
            "expected_keywords": ["growth", "career", "goals", "development"]
        }
    ]
}
