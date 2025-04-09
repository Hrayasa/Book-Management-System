# Personal Library Tracker

A web application for managing your personal book collection, tracking reading progress, and organizing your books.

## Features

- User authentication (registration and login)
- Add, view, edit, and delete books
- Track reading status (To Read, Reading, Read)
- Add personal notes to books
- Dynamic search functionality
- Filter books by reading status
- Book categorization

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd personal-library-django
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at `http://127.0.0.1:8000/`

## Project Structure

```
personal-library-django/
├── library_project/         # Main project configuration
├── book_app/               # Main application
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS)
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

## Usage

1. Register a new account or log in with existing credentials
2. Add books to your collection using the "Add Book" button
3. View your book collection on the main page
4. Click on a book to view details and edit information
5. Use the search bar to filter books by title or author
6. Use the status filter to view books by reading status

## Technologies Used

- Django (Backend Framework)
- SQLite (Database)
- HTML/CSS (Frontend)
- JavaScript (Dynamic Features)
- Bootstrap (UI Components)

## Contributing

Feel free to submit issues and enhancement requests! 