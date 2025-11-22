# Setup Instructions

## Prerequisites

- Node.js and npm (for TypeScript designs)
- Python 3.8+ (for Python frontends and backend)

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
```bash
cd backend
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`
