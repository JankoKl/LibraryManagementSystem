# Library Management System
This Library Management System offers users a simple and intuitive interface for searching, reserving, and borrowing books, while enabling librarians to efficiently manage resources and administrative tasks. By introducing advanced tracking and analysis features, the application enhances transparency and control, allowing libraries to better plan and optimize their operations.
![Alt text](screenshots/5e22178d-92c6-4481-82ea-836b65cdfc26.jpg?raw=true "Optional Title")
![Alt text](screenshots/20bc89d3-37b4-49f0-b737-0bfc99c9ae9d.jpg?raw=true "Optional Title")
![Alt text](screenshots/487726bf-3eb4-49aa-9ac4-0b35c5bb0de2.jpg?raw=true "Optional Title")
### How to run:
virtualenv -p python3 venv\
cd venv\
.\Scripts\activate\
cd [path to project]\
cd LMS\
pip install Django\
python manage.py makemigrations\
python manage.py migrate\
python manage.py runserver
