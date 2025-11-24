# Frontend Designs

A reference library of frontend UI designs and examples for AI projects.

## Purpose

This repository contains various frontend designs and UI patterns that can be referenced when building AI-related projects. All examples use HTML/CSS/JavaScript.

## Tech Stack

**Frontends:**
- HTML/CSS/JavaScript

**Backend:**
- FastAPI (Python)
- SQLite (for database examples)

## Structure

```
frontend-designs/
├── landing-pages/      # Landing page designs
├── blog-pages/         # Blog post designs
├── portfolio-pages/    # Portfolio page designs
├── shopping-pages/     # E-commerce page designs
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

# Launch landing page
./launch.py landing <example-name>

# Launch blog page
./launch.py blog <example-name>

# Launch portfolio page
./launch.py portfolio <example-name>

# Launch shopping page
./launch.py shopping <example-name>

# Start backend
./launch.py backend

# Interactive menu (just run without arguments)
./launch.py
```

### Hard Refresh

If you make changes to HTML/CSS/JS files and don't see updates in your browser, you may need to hard refresh:

- **Windows/Linux**: `Ctrl + Shift + R` or `Ctrl + F5`
- **Mac**: `Cmd + Shift + R`
- **Alternative**: Open DevTools (`F12`) and right-click the refresh button, select "Empty Cache and Hard Reload"

Each design example is self-contained in its own directory with its own README.
