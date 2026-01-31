import React, { useState } from 'react'
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api/v1'

function App() {
  const [role, setRole] = useState('')
  const [difficulty, setDifficulty] = useState('medium')
  const [question, setQuestion] = useState('')
  const [userAnswer, setUserAnswer] = useState('')
  const [expectedAnswer, setExpectedAnswer] = useState('')
  const [evaluation, setEvaluation] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const generateQuestion = async () => {
    if (!role) {
      setError('Please enter a job role')
      return
    }

    setLoading(true)
    setError('')
    try {
      const response = await axios.post(`${API_BASE_URL}/interview/question`, {
        role,
        difficulty
      })
      setQuestion(response.data.question)
    } catch (err) {
      setError('Failed to generate question: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  const evaluateAnswer = async () => {
    if (!question || !userAnswer || !expectedAnswer) {
      setError('Please provide all required fields')
      return
    }

    setLoading(true)
    setError('')
    try {
      const response = await axios.post(`${API_BASE_URL}/interview/evaluate`, {
        question,
        user_answer: userAnswer,
        expected_answer: expectedAnswer
      })
      setEvaluation(response.data)
    } catch (err) {
      setError('Failed to evaluate answer: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>AI-Powered Smart Interview System</h1>
      
      {error && <div style={styles.error}>{error}</div>}
      
      <div style={styles.section}>
        <h2>Generate Interview Question</h2>
        <div style={styles.formGroup}>
          <label>Job Role:</label>
          <input
            type="text"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            placeholder="e.g., Senior Developer, Product Manager"
            style={styles.input}
          />
        </div>
        
        <div style={styles.formGroup}>
          <label>Difficulty:</label>
          <select
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            style={styles.select}
          >
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
        </div>
        
        <button
          onClick={generateQuestion}
          disabled={loading}
          style={styles.button}
        >
          {loading ? 'Generating...' : 'Generate Question'}
        </button>
        
        {question && (
          <div style={styles.result}>
            <strong>Generated Question:</strong>
            <p>{question}</p>
          </div>
        )}
      </div>

      <div style={styles.section}>
        <h2>Evaluate Answer</h2>
        <div style={styles.formGroup}>
          <label>Question:</label>
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Enter the interview question"
            style={styles.textarea}
            rows={3}
          />
        </div>
        
        <div style={styles.formGroup}>
          <label>Your Answer:</label>
          <textarea
            value={userAnswer}
            onChange={(e) => setUserAnswer(e.target.value)}
            placeholder="Enter your answer"
            style={styles.textarea}
            rows={5}
          />
        </div>
        
        <div style={styles.formGroup}>
          <label>Expected Answer:</label>
          <textarea
            value={expectedAnswer}
            onChange={(e) => setExpectedAnswer(e.target.value)}
            placeholder="Enter the expected/reference answer"
            style={styles.textarea}
            rows={5}
          />
        </div>
        
        <button
          onClick={evaluateAnswer}
          disabled={loading}
          style={styles.button}
        >
          {loading ? 'Evaluating...' : 'Evaluate Answer'}
        </button>
        
        {evaluation && (
          <div style={styles.evaluation}>
            <h3>Evaluation Results</h3>
            <div style={styles.metric}>
              <strong>Similarity Score:</strong> {evaluation.similarity_percentage.toFixed(2)}%
            </div>
            <div style={styles.metric}>
              <strong>Sentiment:</strong> {evaluation.sentiment.label} (Confidence: {(evaluation.sentiment.confidence * 100).toFixed(2)}%)
            </div>
            <div style={styles.metric}>
              <strong>Final Score:</strong> {evaluation.final_score.toFixed(2)}/100
            </div>
            <div style={styles.feedback}>
              <strong>Feedback:</strong> {evaluation.overall_feedback}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

const styles = {
  container: {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '20px',
    fontFamily: 'Arial, sans-serif'
  },
  title: {
    textAlign: 'center',
    color: '#333',
    marginBottom: '30px'
  },
  section: {
    backgroundColor: '#f5f5f5',
    padding: '20px',
    borderRadius: '8px',
    marginBottom: '20px'
  },
  formGroup: {
    marginBottom: '15px'
  },
  input: {
    width: '100%',
    padding: '10px',
    fontSize: '14px',
    borderRadius: '4px',
    border: '1px solid #ddd',
    boxSizing: 'border-box'
  },
  select: {
    width: '100%',
    padding: '10px',
    fontSize: '14px',
    borderRadius: '4px',
    border: '1px solid #ddd',
    boxSizing: 'border-box'
  },
  textarea: {
    width: '100%',
    padding: '10px',
    fontSize: '14px',
    borderRadius: '4px',
    border: '1px solid #ddd',
    boxSizing: 'border-box',
    fontFamily: 'Arial, sans-serif'
  },
  button: {
    backgroundColor: '#007bff',
    color: 'white',
    padding: '12px 24px',
    fontSize: '16px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    marginTop: '10px'
  },
  result: {
    marginTop: '20px',
    padding: '15px',
    backgroundColor: 'white',
    borderRadius: '4px'
  },
  evaluation: {
    marginTop: '20px',
    padding: '20px',
    backgroundColor: 'white',
    borderRadius: '4px'
  },
  metric: {
    padding: '10px 0',
    borderBottom: '1px solid #eee'
  },
  feedback: {
    marginTop: '15px',
    padding: '15px',
    backgroundColor: '#e3f2fd',
    borderRadius: '4px'
  },
  error: {
    backgroundColor: '#f8d7da',
    color: '#721c24',
    padding: '12px',
    borderRadius: '4px',
    marginBottom: '20px',
    border: '1px solid #f5c6cb'
  }
}

export default App
