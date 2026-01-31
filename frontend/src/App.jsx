/**
 * Main App Component
 */
import React, { useState } from 'react'
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api/v1'

function App() {
  const [stage, setStage] = useState('start') // start, interview, evaluation, results
  const [candidateName, setCandidateName] = useState('')
  const [position, setPosition] = useState('')
  const [sessionId, setSessionId] = useState('')
  const [questions, setQuestions] = useState([])
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
  const [answers, setAnswers] = useState({})
  const [currentAnswer, setCurrentAnswer] = useState('')
  const [evaluation, setEvaluation] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const startInterview = async () => {
    if (!candidateName || !position) {
      setError('Please fill in all fields')
      return
    }

    setLoading(true)
    setError('')

    try {
      const response = await axios.post(`${API_BASE_URL}/interview/start`, {
        candidate_name: candidateName,
        position: position,
        num_questions: 5
      })

      setSessionId(response.data.session_id)
      setQuestions(response.data.questions)
      setStage('interview')
    } catch (err) {
      setError('Failed to start interview: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  const submitAnswer = async () => {
    if (!currentAnswer.trim()) {
      setError('Please provide an answer')
      return
    }

    setLoading(true)
    setError('')

    try {
      const question = questions[currentQuestionIndex]
      
      // Evaluate the answer
      await axios.post(`${API_BASE_URL}/evaluation/evaluate`, {
        session_id: sessionId,
        question_id: question.id,
        answer_text: currentAnswer
      })

      // Store answer
      setAnswers({
        ...answers,
        [question.id]: currentAnswer
      })

      // Move to next question or finish
      if (currentQuestionIndex < questions.length - 1) {
        setCurrentQuestionIndex(currentQuestionIndex + 1)
        setCurrentAnswer('')
      } else {
        // Get final evaluation
        await getFinalEvaluation()
      }
    } catch (err) {
      setError('Failed to submit answer: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  const getFinalEvaluation = async () => {
    setLoading(true)
    setError('')

    try {
      const response = await axios.post(`${API_BASE_URL}/evaluation/final-evaluation`, {
        session_id: sessionId
      })

      setEvaluation(response.data)
      setStage('results')
    } catch (err) {
      setError('Failed to get evaluation: ' + (err.response?.data?.detail || err.message))
    } finally {
      setLoading(false)
    }
  }

  const resetInterview = () => {
    setStage('start')
    setCandidateName('')
    setPosition('')
    setSessionId('')
    setQuestions([])
    setCurrentQuestionIndex(0)
    setAnswers({})
    setCurrentAnswer('')
    setEvaluation(null)
    setError('')
  }

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1>🎯 AI Smart Interview System</h1>
      </header>

      <main style={styles.main}>
        {error && (
          <div style={styles.error}>
            {error}
          </div>
        )}

        {stage === 'start' && (
          <div style={styles.card}>
            <h2>Start Your Interview</h2>
            <div style={styles.form}>
              <input
                type="text"
                placeholder="Your Name"
                value={candidateName}
                onChange={(e) => setCandidateName(e.target.value)}
                style={styles.input}
              />
              <input
                type="text"
                placeholder="Position (e.g., Python Developer)"
                value={position}
                onChange={(e) => setPosition(e.target.value)}
                style={styles.input}
              />
              <button
                onClick={startInterview}
                disabled={loading}
                style={styles.button}
              >
                {loading ? 'Starting...' : 'Start Interview'}
              </button>
            </div>
          </div>
        )}

        {stage === 'interview' && questions.length > 0 && (
          <div style={styles.card}>
            <div style={styles.progress}>
              Question {currentQuestionIndex + 1} of {questions.length}
            </div>
            <h2>{questions[currentQuestionIndex].text}</h2>
            <div style={styles.questionMeta}>
              <span>Category: {questions[currentQuestionIndex].category}</span>
              <span>Difficulty: {questions[currentQuestionIndex].difficulty}</span>
            </div>
            <textarea
              value={currentAnswer}
              onChange={(e) => setCurrentAnswer(e.target.value)}
              placeholder="Type your answer here..."
              style={styles.textarea}
              rows={8}
            />
            <button
              onClick={submitAnswer}
              disabled={loading}
              style={styles.button}
            >
              {loading ? 'Submitting...' : currentQuestionIndex < questions.length - 1 ? 'Next Question' : 'Finish Interview'}
            </button>
          </div>
        )}

        {stage === 'results' && evaluation && (
          <div style={styles.card}>
            <h2>🎉 Interview Complete!</h2>
            
            <div style={styles.results}>
              <div style={styles.scoreCard}>
                <h3>Overall Performance</h3>
                <div style={styles.score}>
                  {(evaluation.average_score * 100).toFixed(1)}%
                </div>
                <div style={styles.grade}>
                  Grade: {evaluation.overall_grade.toUpperCase()}
                </div>
              </div>

              <div style={styles.summary}>
                <h3>Summary</h3>
                <p>{evaluation.summary}</p>
              </div>

              <div style={styles.recommendations}>
                <h3>Recommendations</h3>
                <ul>
                  {evaluation.recommendations.map((rec, idx) => (
                    <li key={idx}>{rec}</li>
                  ))}
                </ul>
              </div>

              <div style={styles.details}>
                <h3>Question-by-Question Breakdown</h3>
                {evaluation.evaluations.map((eval, idx) => (
                  <div key={idx} style={styles.evaluationItem}>
                    <h4>Q{idx + 1}: {eval.question_text}</h4>
                    <p><strong>Your Answer:</strong> {eval.answer_text.substring(0, 150)}...</p>
                    <div style={styles.scores}>
                      <span>Score: {(eval.overall_score * 100).toFixed(1)}%</span>
                      <span>Grade: {eval.grade}</span>
                    </div>
                    <p><em>{eval.feedback}</em></p>
                  </div>
                ))}
              </div>

              <button onClick={resetInterview} style={styles.button}>
                Start New Interview
              </button>
            </div>
          </div>
        )}
      </main>

      <footer style={styles.footer}>
        <p>© 2024 AI Smart Interview System - Powered by AI</p>
      </footer>
    </div>
  )
}

const styles = {
  container: {
    minHeight: '100vh',
    backgroundColor: '#f5f5f5',
    display: 'flex',
    flexDirection: 'column',
  },
  header: {
    backgroundColor: '#2c3e50',
    color: 'white',
    padding: '1.5rem',
    textAlign: 'center',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
  },
  main: {
    flex: 1,
    padding: '2rem',
    maxWidth: '900px',
    margin: '0 auto',
    width: '100%',
  },
  card: {
    backgroundColor: 'white',
    borderRadius: '8px',
    padding: '2rem',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
    marginTop: '1rem',
  },
  input: {
    padding: '0.75rem',
    fontSize: '1rem',
    border: '1px solid #ddd',
    borderRadius: '4px',
  },
  textarea: {
    padding: '0.75rem',
    fontSize: '1rem',
    border: '1px solid #ddd',
    borderRadius: '4px',
    fontFamily: 'inherit',
    resize: 'vertical',
  },
  button: {
    padding: '0.75rem 1.5rem',
    fontSize: '1rem',
    backgroundColor: '#3498db',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
  },
  progress: {
    fontSize: '0.9rem',
    color: '#7f8c8d',
    marginBottom: '1rem',
  },
  questionMeta: {
    display: 'flex',
    gap: '1rem',
    fontSize: '0.9rem',
    color: '#7f8c8d',
    marginBottom: '1rem',
  },
  results: {
    marginTop: '1rem',
  },
  scoreCard: {
    textAlign: 'center',
    padding: '2rem',
    backgroundColor: '#ecf0f1',
    borderRadius: '8px',
    marginBottom: '1.5rem',
  },
  score: {
    fontSize: '3rem',
    fontWeight: 'bold',
    color: '#2c3e50',
    margin: '0.5rem 0',
  },
  grade: {
    fontSize: '1.2rem',
    color: '#7f8c8d',
    textTransform: 'uppercase',
    fontWeight: 'bold',
  },
  summary: {
    marginBottom: '1.5rem',
  },
  recommendations: {
    marginBottom: '1.5rem',
  },
  details: {
    marginTop: '2rem',
  },
  evaluationItem: {
    padding: '1rem',
    backgroundColor: '#f8f9fa',
    borderRadius: '4px',
    marginBottom: '1rem',
  },
  scores: {
    display: 'flex',
    gap: '1rem',
    fontSize: '0.9rem',
    color: '#7f8c8d',
    marginTop: '0.5rem',
  },
  error: {
    backgroundColor: '#e74c3c',
    color: 'white',
    padding: '1rem',
    borderRadius: '4px',
    marginBottom: '1rem',
  },
  footer: {
    backgroundColor: '#2c3e50',
    color: 'white',
    padding: '1rem',
    textAlign: 'center',
  },
}

export default App
