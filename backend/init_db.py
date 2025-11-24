import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    bio TEXT,
    avatar TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    excerpt TEXT,
    author TEXT NOT NULL,
    date TEXT NOT NULL,
    category TEXT,
    image TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    category TEXT,
    image TEXT,
    stock INTEGER DEFAULT 0
)''')

c.execute('''CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    tech_stack TEXT,
    link TEXT,
    image TEXT,
    year INTEGER
)''')

# Insert sample users
users = [
    ('Sarah Chen', 'sarah@example.com', 'Full-stack developer passionate about building elegant solutions', '👩‍💻'),
    ('Alex Rivera', 'alex@example.com', 'UI/UX designer and frontend developer', '👨‍🎨'),
    ('Jordan Kim', 'jordan@example.com', 'Tech writer and software engineer', '✍️'),
]
c.executemany('INSERT INTO users (name, email, bio, avatar) VALUES (?, ?, ?, ?)', users)

# Insert sample blog posts
posts = [
    ('Building Scalable Microservices', '''# Building Scalable Microservices

Microservices architecture has become the de facto standard for building modern applications. In this article, we'll explore best practices for designing and implementing scalable microservices.

## Key Principles

1. **Single Responsibility**: Each service should do one thing well
2. **Loose Coupling**: Services should be independent
3. **High Cohesion**: Related functionality should be grouped together

## Implementation Strategy

Start with a monolith and extract services as needed. This approach reduces complexity and allows you to identify natural service boundaries.

### Communication Patterns

- REST APIs for synchronous communication
- Message queues for asynchronous operations
- Event-driven architecture for real-time updates

## Conclusion

Microservices offer flexibility and scalability, but they come with operational complexity. Choose this architecture when the benefits outweigh the costs.''',
        'Learn how to design and implement scalable microservices architecture for modern applications.',
        'Sarah Chen', '2025-01-15', 'Architecture', '🏗️'),
    
    ('Modern CSS Techniques', '''# Modern CSS Techniques

CSS has evolved significantly in recent years. Let's explore modern techniques that make styling easier and more powerful.

## Grid and Flexbox

CSS Grid and Flexbox have revolutionized layout design. Grid excels at two-dimensional layouts, while Flexbox is perfect for one-dimensional arrangements.

```css
.container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}
```

## Custom Properties

CSS variables make theming and dynamic styling straightforward:

```css
:root {
    --primary-color: #3b82f6;
    --spacing: 1rem;
}
```

## Container Queries

The future of responsive design allows components to adapt based on their container size, not just viewport width.

## Conclusion

Modern CSS provides powerful tools for creating responsive, maintainable designs. Embrace these techniques to write better stylesheets.''',
        'Discover modern CSS techniques including Grid, Flexbox, custom properties, and container queries.',
        'Alex Rivera', '2025-01-18', 'CSS', '🎨'),
    
    ('Introduction to Machine Learning', '''# Introduction to Machine Learning

Machine learning is transforming how we build software. This guide introduces core concepts and practical applications.

## What is Machine Learning?

ML enables computers to learn from data without explicit programming. It's powered by algorithms that identify patterns and make predictions.

## Types of Machine Learning

- **Supervised Learning**: Training with labeled data
- **Unsupervised Learning**: Finding patterns in unlabeled data
- **Reinforcement Learning**: Learning through trial and error

## Getting Started

Python is the most popular language for ML, with libraries like:

- TensorFlow and PyTorch for deep learning
- Scikit-learn for traditional ML algorithms
- Pandas for data manipulation

## Real-World Applications

ML powers recommendation systems, fraud detection, image recognition, and natural language processing.

## Next Steps

Start with simple projects like linear regression or classification. Build your intuition before tackling complex neural networks.''',
        'A beginner-friendly introduction to machine learning concepts and practical applications.',
        'Jordan Kim', '2025-01-20', 'AI', '🤖'),
    
    ('API Design Best Practices', '''# API Design Best Practices

Well-designed APIs are intuitive, consistent, and easy to use. Let's explore principles for creating excellent APIs.

## RESTful Principles

- Use HTTP methods correctly (GET, POST, PUT, DELETE)
- Design resource-oriented URLs
- Return appropriate status codes
- Version your API

## Naming Conventions

Use clear, consistent naming:

```
GET /api/users
GET /api/users/{id}
POST /api/users
PUT /api/users/{id}
DELETE /api/users/{id}
```

## Error Handling

Return meaningful error messages with proper status codes:

```json
{
    "error": "User not found",
    "code": "USER_NOT_FOUND",
    "status": 404
}
```

## Documentation

Great documentation is essential. Include examples, error codes, and authentication details.

## Conclusion

Invest time in API design upfront. A well-designed API reduces support burden and improves developer experience.''',
        'Essential best practices for designing clean, intuitive, and maintainable APIs.',
        'Sarah Chen', '2025-01-22', 'Backend', '🔌'),
    
    ('JavaScript Performance Tips', '''# JavaScript Performance Tips

Performance matters. Slow applications frustrate users and hurt business metrics. Here's how to optimize JavaScript performance.

## Minimize DOM Manipulation

DOM operations are expensive. Batch updates and use document fragments:

```javascript
const fragment = document.createDocumentFragment();
items.forEach(item => {
    const el = document.createElement('div');
    el.textContent = item;
    fragment.appendChild(el);
});
container.appendChild(fragment);
```

## Debounce and Throttle

Limit expensive operations like API calls or scroll handlers:

```javascript
const debounce = (fn, delay) => {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => fn(...args), delay);
    };
};
```

## Use Web Workers

Offload heavy computations to background threads to keep the UI responsive.

## Lazy Loading

Load resources only when needed. This reduces initial bundle size and improves load times.

## Conclusion

Small optimizations compound. Profile your application, identify bottlenecks, and optimize strategically.''',
        'Practical tips for optimizing JavaScript performance and creating faster web applications.',
        'Alex Rivera', '2025-01-25', 'JavaScript', '⚡'),
]

c.executemany('INSERT INTO posts (title, content, excerpt, author, date, category, image) VALUES (?, ?, ?, ?, ?, ?, ?)', posts)

# Insert sample products
products = [
    ('Wireless Headphones Pro', 199.99, 'Premium noise-canceling headphones with 30-hour battery life', 'Electronics', '🎧', 45),
    ('Smart Watch Ultra', 349.99, 'Advanced fitness tracking with heart rate monitor and GPS', 'Electronics', '⌚', 32),
    ('Laptop Stand Aluminum', 49.99, 'Ergonomic laptop stand with adjustable height', 'Accessories', '💻', 78),
    ('Mechanical Keyboard RGB', 129.99, 'Cherry MX switches with customizable RGB lighting', 'Electronics', '⌨️', 56),
    ('USB-C Hub 7-in-1', 39.99, 'Multi-port hub with HDMI, USB 3.0, and SD card reader', 'Accessories', '🔌', 120),
    ('Wireless Mouse Ergonomic', 59.99, 'Comfortable ergonomic design with precision tracking', 'Electronics', '🖱️', 89),
    ('Webcam 4K Pro', 149.99, 'Crystal clear 4K video with auto-focus and noise reduction', 'Electronics', '📷', 41),
    ('Phone Stand Adjustable', 24.99, 'Foldable phone stand for desk or travel', 'Accessories', '📱', 156),
    ('Portable SSD 1TB', 119.99, 'Fast external storage with USB-C connectivity', 'Storage', '💾', 67),
    ('Cable Organizer Set', 14.99, 'Keep your cables tidy with this 10-piece organizer set', 'Accessories', '🔗', 203),
    ('Monitor Light Bar', 79.99, 'Reduce eye strain with adjustable LED monitor lighting', 'Accessories', '💡', 38),
    ('Desk Mat XXL', 34.99, 'Extra large desk mat with smooth surface and stitched edges', 'Accessories', '🖼️', 94),
]

c.executemany('INSERT INTO products (name, price, description, category, image, stock) VALUES (?, ?, ?, ?, ?, ?)', products)

# Insert sample projects
projects = [
    ('E-commerce Platform', 'Full-stack e-commerce solution with payment integration and inventory management', 'React, Node.js, PostgreSQL, Stripe', 'https://github.com/example/ecommerce', '🛒', 2024),
    ('Task Management App', 'Collaborative task manager with real-time updates and team features', 'Vue.js, Firebase, Tailwind CSS', 'https://github.com/example/taskapp', '✅', 2024),
    ('Weather Dashboard', 'Beautiful weather dashboard with forecasts and historical data', 'React, OpenWeather API, Chart.js', 'https://github.com/example/weather', '🌤️', 2023),
    ('Portfolio Generator', 'Static site generator for creating developer portfolios', 'Python, Jinja2, Markdown', 'https://github.com/example/portfolio-gen', '📄', 2023),
    ('Chat Application', 'Real-time chat with rooms, direct messages, and file sharing', 'Socket.io, Express, MongoDB', 'https://github.com/example/chat', '💬', 2024),
    ('Fitness Tracker', 'Track workouts, nutrition, and progress with data visualization', 'React Native, Node.js, MySQL', 'https://github.com/example/fitness', '💪', 2023),
]

c.executemany('INSERT INTO projects (title, description, tech_stack, link, image, year) VALUES (?, ?, ?, ?, ?, ?)', projects)

conn.commit()
conn.close()

print("Database initialized successfully!")
print("Created tables: users, posts, products, projects")
print(f"Inserted: {len(users)} users, {len(posts)} posts, {len(products)} products, {len(projects)} projects")
