# Setup Instructions

## Prerequisites

- Node.js and npm (for TypeScript designs)
- Python 3.8+ (for Python frontends and backend)

## WSL Users

If using WSL, configure your browser for auto-opening:

```bash
# Add to ~/.zshrc or ~/.bashrc
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
```

Then reload: `source ~/.zshrc`

## TypeScript Setup

```bash
npm install
```

This installs TypeScript and common tooling for the TypeScript designs.

## Python Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running Examples

### HTML/CSS/JS
Simply open the `index.html` file in a browser, or use a local server:
```bash
python3 -m http.server 8000
```

### TypeScript Designs
Each TypeScript design will have its own setup instructions in its directory.

### Python Frontends (Gradio/Streamlit)
```bash
# Gradio
python app.py

# Streamlit
streamlit run app.py
```

### Backend

1. Initialize the database:
```bash
cd backend
python3 init_db.py
```

2. Start the backend:
```bash
uvicorn app:app --reload
```

Or use the launcher:
```bash
./launch.py backend
```

The backend will be available at `http://localhost:8000`
API docs at `http://localhost:8000/docs`
