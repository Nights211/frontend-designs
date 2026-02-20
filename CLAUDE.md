# CLAUDE.md

## What This Repo Is

A library of self-contained frontend UI designs organized by page type. Used for testing and comparing different visual styles and layouts. Each design lives in its own directory with at minimum `index.html` + `style.css`.

## Repo Layout

```
landing-pages/<name>/     # Landing page designs
blog-pages/<name>/        # Blog page designs
portfolio-pages/<name>/   # Portfolio page designs
shopping-pages/<name>/    # Shopping/e-commerce page designs
backend/                  # Shared FastAPI + SQLite backend
launch.py                 # Launcher script (auto-discovers designs)
kill-servers.py           # Kills servers on ports 8000/8001
```

## How Designs Work

Each design directory contains:
- `index.html` - the page (required)
- `style.css` - styles (required)
- `README.md` - description of the design (optional)
- `content.md` / `projects.md` - markdown content for data-driven designs (optional)
- `script.js` - separate JS file if needed (optional)

Designs are either **static** (just HTML/CSS) or **API-driven** (fetch data from the backend).

## Backend API

The backend runs on **port 8001** when auto-started by `launch.py`, or **port 8000** when launched standalone.

Endpoints:
- `GET /api/posts` and `/api/posts/{id}` - blog post data
- `GET /api/products` and `/api/products/{id}` - product data
- `GET /api/projects` and `/api/projects/{id}` - project data
- `GET /api/users` and `/api/users/{id}` - user data

Initialize the database: `python backend/init_db.py`

## Adding a New Design

1. Create a directory: `<category>-pages/<design-name>/`
2. Add `index.html` and `style.css` at minimum
3. The launcher auto-discovers it — no registration needed
4. For API-driven designs, fetch from `http://localhost:8001/api/...`
5. For markdown-driven designs, use `marked.js` CDN and load a local `.md` file

## Running Designs

```bash
./launch.py                              # Interactive menu
./launch.py <category> <design-name>     # Direct launch
./launch.py list                         # Show all designs
./launch.py backend                      # Start backend only
```

Categories: `landing`, `blog`, `portfolio`, `shopping`

Frontend server runs on port 8000, backend on port 8001.

## Conventions

- All frontends use vanilla HTML/CSS/JS — no frameworks, no build steps
- CSS goes in a separate `style.css` file, not inline
- Designs should be self-contained (no shared CSS between designs)
- Use descriptive directory names (e.g., `blog-dark-minimal`, `shop-premium-electronics`)
- Use the `/frontend-design` skill in Claude Code to generate new designs

## Python Environment

- Uses `uv` for dependency management (`uv sync` to install)
- `.envrc` auto-activates venv via direnv
- Dependencies: fastapi, uvicorn, sqlalchemy, aiosqlite
