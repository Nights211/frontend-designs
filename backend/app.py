from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from typing import List, Dict, Any

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def root():
    return {"message": "Frontend Designs API"}

@app.get("/api/posts")
def get_posts():
    conn = get_db()
    posts = conn.execute("SELECT * FROM posts ORDER BY date DESC").fetchall()
    conn.close()
    return [dict(post) for post in posts]

@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    conn = get_db()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    return dict(post) if post else None

@app.get("/api/products")
def get_products():
    conn = get_db()
    products = conn.execute("SELECT * FROM products ORDER BY id").fetchall()
    conn.close()
    return [dict(product) for product in products]

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    conn = get_db()
    product = conn.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
    conn.close()
    return dict(product) if product else None

@app.get("/api/projects")
def get_projects():
    conn = get_db()
    projects = conn.execute("SELECT * FROM projects ORDER BY id").fetchall()
    conn.close()
    return [dict(project) for project in projects]

@app.get("/api/projects/{project_id}")
def get_project(project_id: int):
    conn = get_db()
    project = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    conn.close()
    return dict(project) if project else None

@app.get("/api/users")
def get_users():
    conn = get_db()
    users = conn.execute("SELECT * FROM users ORDER BY id").fetchall()
    conn.close()
    return [dict(user) for user in users]

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return dict(user) if user else None
