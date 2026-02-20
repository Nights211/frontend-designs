# Frontend Designs

A reference library of frontend UI designs for testing different visual styles and layouts. Each design is self-contained and can be viewed in a browser.

## Quick Start

```bash
# Interactive menu - pick a design to launch
./launch.py

# Or launch directly by category and name
./launch.py landing <design-name>
./launch.py blog <design-name>
./launch.py portfolio <design-name>
./launch.py shopping <design-name>

# List all available examples
./launch.py list

# Start just the backend API
./launch.py backend
```

The launcher starts a local HTTP server on port 8000 and opens your browser. Designs that need the backend API will auto-start it on port 8001.

## Adding a New Design

1. Create a directory under the right category folder:
   ```
   landing-pages/my-new-design/
   blog-pages/my-new-design/
   portfolio-pages/my-new-design/
   shopping-pages/my-new-design/
   ```

2. Add at minimum `index.html` and `style.css`. The launcher auto-discovers new directories.

3. Optionally add a `README.md` describing the design.

4. If the design needs dynamic data, fetch from `http://localhost:8001/api/...` (posts, products, projects, users).

## Structure

```
frontend-designs/
├── landing-pages/          # Landing page designs
├── blog-pages/             # Blog post designs
├── portfolio-pages/        # Portfolio page designs
├── shopping-pages/         # E-commerce page designs
├── backend/                # Shared FastAPI backend + SQLite
│   ├── app.py              # REST API endpoints
│   ├── init_db.py          # Database schema + seed data
│   └── database.db         # SQLite database
├── launch.py               # Launcher script (interactive or CLI)
├── kill-servers.py         # Kill servers on ports 8000/8001
├── SETUP.md                # Detailed setup instructions
└── README.md               # This file
```

## Tech Stack

- **Frontends:** HTML, CSS, vanilla JavaScript
- **Backend:** FastAPI + SQLite (Python)
- **Content:** Some designs use `marked.js` to render markdown files
- **Tooling:** `uv` for Python deps, `direnv` for auto-activating venv

## Hard Refresh

If changes don't appear in the browser:
- **Windows/Linux:** `Ctrl + Shift + R`
- **Mac:** `Cmd + Shift + R`

## Setup

See [SETUP.md](SETUP.md) for prerequisites and installation.
