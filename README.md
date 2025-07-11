# Library Management System

A web-based Library Management System built with Django that allows users to search, reserve, and borrow books through an intuitive interface. Librarians can manage books, monitor borrowing activity, and maintain an efficient and organized library workflow.

![Home Page](screenshots/5e22178d-92c6-4481-82ea-836b65cdfc26.jpg?raw=true)
![Dashboard](screenshots/20bc89d3-37b4-49f0-b737-0bfc99c9ae9d.jpg?raw=true)
![Book List](screenshots/487726bf-3eb4-49aa-9ac4-0b35c5bb0de2.jpg?raw=true)

---

## Features

- Search and browse available books
- Borrow and reserve books
- Librarian panel to manage books and users
- Transparent record tracking and analytics
- Organized static assets and clean UI

---

## Technologies used:

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (Bootstrap), JS
- **Database:** SQLite 
- **Deployment:** [Render](https://render.com/) 

---

## Live Demo

 [Live Website](https://librarymanagementsystem-725y.onrender.com)

---

### Run it locally:
pip install -r requirements.txt
virtualenv -p python3 venv\
cd venv\
.\Scripts\activate\
cd [path to project]\
cd LMS\
pip install Django\
python manage.py makemigrations\
python manage.py migrate\
python manage.py runserver
