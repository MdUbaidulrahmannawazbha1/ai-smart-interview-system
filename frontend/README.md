# AI Smart Interview System - Frontend

## Overview

React-based frontend for the AI Smart Interview System, providing an interactive interview experience.

## Features

- 🎨 Clean and intuitive user interface
- 📝 Multi-step interview flow
- 📊 Real-time score display
- 💬 Detailed feedback and recommendations
- 📱 Responsive design

## Technology Stack

- **Framework**: React 18
- **Build Tool**: Vite
- **HTTP Client**: Axios
- **Styling**: Inline CSS (easily replaceable with CSS modules or styled-components)

## Installation

1. **Install dependencies**:
```bash
cd frontend
npm install
```

## Running the Application

### Development Mode
```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### Production Build
```bash
npm run build
npm run preview
```

## Project Structure

```
frontend/
├── src/
│   ├── App.jsx          # Main application component
│   └── main.jsx         # Entry point
├── package.json         # Dependencies and scripts
└── README.md
```

## Application Flow

1. **Start**: Enter candidate name and position
2. **Interview**: Answer questions one by one
3. **Evaluation**: System evaluates answers in real-time
4. **Results**: View comprehensive evaluation and feedback

## Component Overview

### App Component

Main component managing:
- Interview stages (start, interview, results)
- API communication
- State management
- User interactions

## Configuration

Update `API_BASE_URL` in `App.jsx` to point to your backend:
```javascript
const API_BASE_URL = 'http://localhost:8000/api/v1'
```

## Development

### Adding New Features

1. Update state in App component
2. Add new UI sections
3. Connect to backend APIs using axios

### Styling

Current implementation uses inline styles for simplicity. For larger applications, consider:
- CSS Modules
- Styled Components
- Tailwind CSS

## API Integration

The frontend communicates with the backend through these endpoints:
- `/interview/start` - Start interview
- `/evaluation/evaluate` - Evaluate answers
- `/evaluation/final-evaluation` - Get final results

## Future Enhancements

- [ ] Audio recording for voice answers
- [ ] Timer for each question
- [ ] Progress saving
- [ ] Interview history
- [ ] User authentication
- [ ] Accessibility improvements
