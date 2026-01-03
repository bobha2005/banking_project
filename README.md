🏦 DABank - Secure Banking System
A modern, full-stack banking application featuring a React frontend and a Python Flask backend. DABank offers a "Fintech-style" elegant interface with real-time balance updates and transaction tracking.

✨ New Features
Glassmorphism UI: A premium, semi-transparent interface with blurred background effects for a modern look.

Staggered History Animations: Transaction history items now "waterfall" into view with smooth CSS entrance animations.

Smart Navigation: Perfectly centered operation buttons and a pinned floating Logout button for better accessibility.

Smooth Scroll Engine: Native smooth scrolling implemented for seamless navigation between the dashboard and transaction history.

🚀 Local Setup Guide
1. Backend (Python Flask)
Navigate to the backend folder: cd backend

Create and activate a virtual environment: python3 -m venv venv source venv/bin/activate

Install dependencies: pip install flask flask-cors

Run the server: python server.py The server will run on http://localhost:5001

2. Frontend (React)
Navigate to the frontend folder: cd frontend

Install packages: npm install

Start the app: npm start The app will open on http://localhost:3000 (or 3002)

🌐 Deployment Instructions
Backend (Render/Railway)
Ensure you have a requirements.txt file (Generate via pip freeze > requirements.txt).

Update server.py to use os.environ.get("PORT") for the port setting.

Connect your GitHub repository to Render and set the start command to python backend/server.py.

Frontend (Vercel/Netlify)
In App.js, update the API_BASE variable from localhost:5001 to your live Backend URL.

Connect your repository to Vercel.

Update your Backend CORS settings to allow requests from your new Vercel domain.

🛠 Tech Stack
Frontend: React.js, CSS3 (Flexbox & Animations)

Backend: Python 3, Flask, Flask-CORS

Database: Local JSON (or current banking logic)

Typography: Montserrat & Inter
