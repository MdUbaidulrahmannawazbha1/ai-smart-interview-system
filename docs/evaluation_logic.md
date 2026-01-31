# Evaluation Logic

## Overview

The evaluation system uses multiple AI/ML techniques to assess interview answers comprehensively.

## Scoring Components

### 1. Semantic Similarity (40% weight)

**Method**: TF-IDF Vectorization + Cosine Similarity

**Process**:
1. Convert question and answer text to TF-IDF vectors
2. Calculate cosine similarity between vectors
3. Score range: 0.0 to 1.0

**Purpose**: Measures how well the answer addresses the question semantically

### 2. Keyword Match (40% weight)

**Method**: Custom Keyword Extraction and Matching

**Process**:
1. Extract keywords from answer (filter stop words)
2. Compare with expected technical keywords
3. Calculate match percentage
4. Score range: 0.0 to 1.0

**Purpose**: Verifies coverage of important technical terms and concepts

### 3. Sentiment Analysis (20% weight)

**Method**: Transformer-based Sentiment Model (DistilBERT)

**Process**:
1. Analyze text sentiment (POSITIVE/NEGATIVE)
2. Convert to normalized score
3. Score range: 0.0 to 1.0

**Purpose**: Assesses confidence, clarity, and communication quality

## Overall Score Calculation

```
Overall Score = (0.4 × Similarity) + (0.4 × Keywords) + (0.2 × Sentiment)
```

## Grading System

| Grade | Score Range | Description |
|-------|-------------|-------------|
| Excellent | ≥0.80 | Outstanding understanding and communication |
| Good | 0.60-0.79 | Solid understanding with minor gaps |
| Average | 0.40-0.59 | Basic understanding, needs improvement |
| Poor | <0.40 | Insufficient understanding |

## Feedback Generation

Feedback is dynamically generated based on:
- Overall grade level
- Individual component scores
- Specific weaknesses identified

### Feedback Components

1. **Overall Assessment**: Based on final grade
2. **Similarity Feedback**: If score < 0.4, suggests better question comprehension
3. **Keyword Feedback**: If score < 0.4, recommends more technical terms
4. **Sentiment Feedback**: If score < 0.4, suggests more confidence

## Final Evaluation

The final evaluation aggregates all question evaluations:

1. **Average Score**: Mean of all question scores
2. **Overall Grade**: Based on average score
3. **Summary**: Narrative summary of performance
4. **Recommendations**: Personalized improvement suggestions

### Recommendation Logic

- **Strong Performance (≥70%)**: Encouragement and advanced suggestions
- **Moderate Performance (50-70%)**: Practice and concept review
- **Weak Performance (<50%)**: Fundamental study and mentorship

## Example Evaluation

**Question**: "Explain Python decorators"
**Answer**: "Decorators in Python are functions that modify other functions. They use the @ syntax and allow you to add functionality to existing code without modifying it."

**Scores**:
- Similarity: 0.72 (answer relates well to question)
- Keywords: 0.75 (contains "decorators", "functions", "syntax")
- Sentiment: 0.68 (confident, clear tone)
- **Overall: 0.72 (Good)**

**Feedback**: "Good answer with solid understanding of the topic. You covered the key points well."
