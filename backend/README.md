# Backend API

Shared FastAPI backend with SQLite database for all frontend examples.

## Setup

1. Initialize the database:
```bash
cd backend
python init_db.py
```

2. Start the server:
```bash
uvicorn app:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Posts (Blog)
- `GET /api/posts` - Get all blog posts
- `GET /api/posts/{id}` - Get single post

### Products (E-commerce)
- `GET /api/products` - Get all products
- `GET /api/products/{id}` - Get single product

### Projects (Portfolio)
- `GET /api/projects` - Get all projects
- `GET /api/projects/{id}` - Get single project

### Users
- `GET /api/users` - Get all users
- `GET /api/users/{id}` - Get single user

## Database Schema

### users
- id, name, email, bio, avatar

### posts
- id, title, content, excerpt, author, date, category, image

### products
- id, name, price, description, category, image, stock

### projects
- id, title, description, tech_stack, link, image, year

## Usage in Frontend

```javascript
// Fetch blog posts
fetch('http://localhost:8000/api/posts')
    .then(r => r.json())
    .then(posts => console.log(posts));

// Fetch products
fetch('http://localhost:8000/api/products')
    .then(r => r.json())
    .then(products => console.log(products));
```

## CORS

CORS is enabled for all origins to allow frontend examples to access the API from any port.
