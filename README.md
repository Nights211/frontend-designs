# Frontend Designs

A reference library of frontend UI designs and examples for AI projects.

## Purpose

This repository contains various frontend designs and UI patterns that can be referenced when building AI-related projects. It includes examples across multiple technologies and frameworks.

## Tech Stack

**Frontends:**
- HTML/CSS/JavaScript
- TypeScript (React, Vue, etc.)
- Python (Gradio, Streamlit)

**Backend:**
- FastAPI (Python)
- SQLite (for database examples)

## Structure

```
frontend-designs/
├── html-css-js/        # Pure HTML/CSS/JS designs
├── typescript-designs/ # TypeScript-based UIs
├── python-frontends/   # Gradio and Streamlit UIs
├── backend/            # Shared FastAPI backend with SQLite
├── SETUP.md            # Setup instructions
└── README.md           # This file
```

## Quick Start

See [SETUP.md](SETUP.md) for installation and setup instructions.

### Launcher Script

Use the launcher script to quickly run examples:

```bash
# List all examples
./launch.py list

# Launch HTML example
./launch.py html landing-page-01

# Launch Gradio app
./launch.py gradio <example-name>

# Launch Streamlit app
./launch.py streamlit <example-name>

# Start backend
./launch.py backend
```

Each design example is self-contained in its own directory with its own README.
