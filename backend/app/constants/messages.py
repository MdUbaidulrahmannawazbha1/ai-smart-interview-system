"""
messages.py

Constants module for user-facing messages in AI-Powered Smart Interview System.
Defines standardized messages, prompts, and feedback templates.
"""

# API Response Messages
SUCCESS_MESSAGES = {
    "question_generated": "Interview question generated successfully",
    "answer_evaluated": "Answer evaluated successfully",
    "session_created": "Interview session created successfully",
    "session_completed": "Interview session completed successfully",
}

ERROR_MESSAGES = {
    "invalid_input": "Invalid input provided",
    "evaluation_failed": "Failed to evaluate answer",
    "question_generation_failed": "Failed to generate question",
    "audio_processing_failed": "Failed to process audio file",
    "invalid_audio_format": "Unsupported audio format",
    "file_too_large": "File size exceeds maximum allowed size",
    "missing_required_field": "Required field is missing",
}

# Feedback Templates
FEEDBACK_TEMPLATES = {
    "excellent": "Excellent performance! Your answer demonstrates deep understanding and strong communication skills.",
    "good": "Good performance! Your answer shows solid understanding with room for minor improvements.",
    "fair": "Fair performance. Your answer covers the basics but could be more detailed and comprehensive.",
    "poor": "Needs improvement. Your answer lacks sufficient detail and understanding of the topic.",
}

# Performance Level Thresholds
PERFORMANCE_THRESHOLDS = {
    "excellent": 80.0,
    "good": 60.0,
    "fair": 40.0,
    "poor": 0.0,
}

# Question Generation Prompts
QUESTION_PROMPTS = {
    "technical": {
        "easy": "Explain the basic concepts of {topic}",
        "medium": "Describe your approach to solving {topic} problems",
        "hard": "Design a solution for a complex {topic} scenario",
    },
    "behavioral": {
        "easy": "Tell me about a time when you {situation}",
        "medium": "How do you handle {situation} in a team environment?",
        "hard": "Describe a challenging {situation} and how you resolved it",
    },
}

# Validation Messages
VALIDATION_MESSAGES = {
    "empty_answer": "Answer cannot be empty",
    "answer_too_short": "Answer is too short. Please provide more details.",
    "invalid_difficulty": "Difficulty must be 'easy', 'medium', or 'hard'",
    "invalid_role": "Please specify a valid job role",
}

# System Messages
SYSTEM_MESSAGES = {
    "welcome": "Welcome to AI-Powered Smart Interview System",
    "session_start": "Interview session starting...",
    "session_end": "Interview session completed. Generating feedback...",
    "processing": "Processing your response...",
}

# Recommendation Templates
RECOMMENDATIONS = {
    "improve_technical": "Consider deepening your technical knowledge in this area",
    "improve_communication": "Work on articulating your thoughts more clearly",
    "improve_detail": "Provide more specific examples and details in your answers",
    "improve_structure": "Try to structure your answers more logically",
    "good_performance": "Keep up the excellent work!",
}
