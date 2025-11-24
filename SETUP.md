# Setup Instructions

## Prerequisites

- Node.js and npm (for TypeScript designs)
- Python 3.8+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager
- [direnv](https://direnv.net/) - Auto-load environment (optional but recommended)

## WSL Users

If using WSL, configure your browser for auto-opening:

```bash
# Add to ~/.zshrc or ~/.bashrc
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
```

Then reload: `source ~/.zshrc`

## Python Setup

### Install uv (if not already installed)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup with direnv (recommended)
```bash
# Install dependencies and create virtual environment
uv sync

# Allow direnv to auto-activate the venv
direnv allow
```

Now the virtual environment will automatically activate when you `cd` into this directory.

### Setup without direnv
```bash
# Install dependencies and create virtual environment
uv sync

# Manually activate the venv
source .venv/bin/activate
```

## TypeScript Setup

```bash
npm install
```

This installs TypeScript and common tooling for the TypeScript designs.

## Running Examples

### HTML/CSS/JS
Simply open the `index.html` file in a browser, or use a local server:
```bash
python -m http.server 8000
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
python backend/init_db.py
```

2. Start the backend:
```bash
uvicorn backend.app:app --reload
```

Or use the launcher:
```bash
./launch.py backend
```

The backend will be available at `http://localhost:8000`
API docs at `http://localhost:8000/docs`

## Adding Dependencies

```bash
# Add a new package
uv add package-name

# Add a dev dependency
uv add --dev package-name
```
