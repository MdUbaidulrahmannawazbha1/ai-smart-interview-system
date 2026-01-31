import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [systemStatus, setSystemStatus] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    // Fetch system status from backend
    axios.get('http://localhost:8000/')
      .then(response => {
        setSystemStatus(response.data)
        setLoading(false)
      })
      .catch(err => {
        setError('Failed to connect to backend')
        setLoading(false)
      })
  }, [])

  return (
    <div style={{ 
      fontFamily: 'Arial, sans-serif', 
      maxWidth: '1200px', 
      margin: '0 auto', 
      padding: '20px' 
    }}>
      <header style={{
        textAlign: 'center',
        padding: '40px 0',
        borderBottom: '2px solid #e0e0e0',
        marginBottom: '40px'
      }}>
        <h1 style={{ 
          fontSize: '2.5em', 
          marginBottom: '10px',
          color: '#333'
        }}>
          🎯 AI Smart Interview System
        </h1>
        <p style={{ 
          fontSize: '1.2em', 
          color: '#666' 
        }}>
          Intelligent Interview Platform powered by AI
        </p>
      </header>

      <main>
        <section style={{
          backgroundColor: '#f5f5f5',
          padding: '30px',
          borderRadius: '10px',
          marginBottom: '30px'
        }}>
          <h2 style={{ marginTop: 0, color: '#333' }}>System Status</h2>
          {loading && (
            <p style={{ fontSize: '1.1em', color: '#666' }}>
              🔄 Loading system status...
            </p>
          )}
          {error && (
            <div style={{
              backgroundColor: '#ffebee',
              border: '1px solid #ef5350',
              padding: '15px',
              borderRadius: '5px',
              color: '#c62828'
            }}>
              <strong>⚠️ Error:</strong> {error}
              <p style={{ marginTop: '10px', marginBottom: 0 }}>
                Make sure the backend server is running on http://localhost:8000
              </p>
            </div>
          )}
          {systemStatus && (
            <div style={{
              backgroundColor: '#e8f5e9',
              border: '1px solid #66bb6a',
              padding: '15px',
              borderRadius: '5px',
              color: '#2e7d32'
            }}>
              <p style={{ marginTop: 0, fontSize: '1.1em' }}>
                <strong>✅ Status:</strong> {systemStatus.status}
              </p>
              <p style={{ marginBottom: 0, fontSize: '1.1em' }}>
                <strong>🚀 Service:</strong> {systemStatus.service}
              </p>
            </div>
          )}
        </section>

        <section style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '20px',
          marginBottom: '30px'
        }}>
          <div style={{
            backgroundColor: '#e3f2fd',
            padding: '25px',
            borderRadius: '10px',
            border: '1px solid #90caf9'
          }}>
            <h3 style={{ marginTop: 0, color: '#1565c0' }}>📚 API Documentation</h3>
            <p>Explore the API endpoints and test them interactively</p>
            <a 
              href="http://localhost:8000/docs" 
              target="_blank" 
              rel="noopener noreferrer"
              style={{
                display: 'inline-block',
                backgroundColor: '#1976d2',
                color: 'white',
                padding: '10px 20px',
                textDecoration: 'none',
                borderRadius: '5px',
                marginTop: '10px'
              }}
            >
              Open Swagger UI
            </a>
          </div>

          <div style={{
            backgroundColor: '#f3e5f5',
            padding: '25px',
            borderRadius: '10px',
            border: '1px solid #ce93d8'
          }}>
            <h3 style={{ marginTop: 0, color: '#6a1b9a' }}>🔍 Alternative Docs</h3>
            <p>View API documentation in ReDoc format</p>
            <a 
              href="http://localhost:8000/redoc" 
              target="_blank" 
              rel="noopener noreferrer"
              style={{
                display: 'inline-block',
                backgroundColor: '#7b1fa2',
                color: 'white',
                padding: '10px 20px',
                textDecoration: 'none',
                borderRadius: '5px',
                marginTop: '10px'
              }}
            >
              Open ReDoc
            </a>
          </div>

          <div style={{
            backgroundColor: '#fff3e0',
            padding: '25px',
            borderRadius: '10px',
            border: '1px solid #ffb74d'
          }}>
            <h3 style={{ marginTop: 0, color: '#e65100' }}>⚡ Features</h3>
            <ul style={{ paddingLeft: '20px' }}>
              <li>AI-powered questions</li>
              <li>Real-time evaluation</li>
              <li>Speech-to-text</li>
              <li>Sentiment analysis</li>
            </ul>
          </div>
        </section>

        <section style={{
          backgroundColor: '#fff',
          padding: '30px',
          borderRadius: '10px',
          border: '1px solid #e0e0e0'
        }}>
          <h2 style={{ marginTop: 0, color: '#333' }}>Getting Started</h2>
          <ol style={{ lineHeight: '1.8', fontSize: '1.1em' }}>
            <li>Ensure both backend and frontend servers are running</li>
            <li>Navigate to the API documentation to explore available endpoints</li>
            <li>Start an interview session using the <code>/api/v1/interview</code> endpoints</li>
            <li>Submit answers for evaluation using the <code>/api/v1/evaluation</code> endpoints</li>
            <li>Check system health at <code>/api/v1/health</code></li>
          </ol>
        </section>
      </main>

      <footer style={{
        textAlign: 'center',
        marginTop: '60px',
        padding: '20px',
        borderTop: '1px solid #e0e0e0',
        color: '#666'
      }}>
        <p>AI Smart Interview System © 2024</p>
      </footer>
    </div>
  )
}

export default App
