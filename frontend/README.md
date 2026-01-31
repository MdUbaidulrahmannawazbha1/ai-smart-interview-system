# AI Smart Interview System - Frontend

React-based frontend application for the AI Smart Interview System.

## Features

- Modern React UI with Vite
- Real-time system status display
- Links to API documentation
- Responsive design

## Running the Frontend

### Quick Start
From the project root:
```bash
./start_frontend.sh
```

### Manual Start
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The application will be available at http://localhost:5173

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## Project Structure

```
frontend/
├── src/
│   ├── App.jsx       # Main application component
│   └── main.jsx      # Application entry point
├── index.html        # HTML template
├── package.json      # Dependencies and scripts
└── vite.config.js    # Vite configuration
```

## Configuration

The frontend is configured to proxy API requests to the backend server at `http://localhost:8000`. This is set up in `vite.config.js`.

## Technologies

- React 18
- Vite
- Axios for HTTP requests
