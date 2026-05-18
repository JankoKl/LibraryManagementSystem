# Library Management System

A web-based Library Management System built with Django that allows users to search, reserve, and borrow books through an intuitive interface. Librarians can manage books, monitor borrowing activity, and maintain an efficient and organized library workflow.

![Home Page](screenshots/5e22178d-92c6-4481-82ea-836b65cdfc26.jpg?raw=true)
![Dashboard](screenshots/20bc89d3-37b4-49f0-b737-0bfc99c9ae9d.jpg?raw=true)
![Book List](screenshots/487726bf-3eb4-49aa-9ac4-0b35c5bb0de2.jpg?raw=true)

## Live Demo
[Live Website](https://librarymanagementsystem-1-ocox.onrender.com/)

---

## Features
- User authentication (login/logout)
- Search and browse available books
- Borrow and reserve books
- Return books
- Librarian panel to manage books and users
- REST API for all resources
- Transparent record tracking and analytics

---

## REST API

Base URL: `https://librarymanagementsystem-1-ocox.onrender.com/api/`

| Endpoint | Methods | Description |
|----------|---------|-------------|
| `/api/books/` | GET, POST, PUT, DELETE | Manage books |
| `/api/students/` | GET, POST, PUT, DELETE | Manage students |
| `/api/book-issues/` | GET, POST, PUT, DELETE | Manage book issues |
| `/api/book-instances/` | GET, POST, PUT, DELETE | Manage book instances |

Example request:
```
GET /api/books/
```
```json
[
    {
        "id": 1,
        "book_title": "Clean Code",
        "book_author": "Robert C. Martin",
        "book_pages": 431,
        "summary": "A handbook of agile software craftsmanship"
    }
]
```

---

## Technologies
- **Backend:** Python, Django, Django REST Framework
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Database:** SQLite
- **Deployment:** Render
- **Authentication:** Django Auth

---

## Run locally
```bash
git clone https://github.com/[tvoj-username]/LibraryManagementSystem.git
cd LibraryManagementSystem
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
