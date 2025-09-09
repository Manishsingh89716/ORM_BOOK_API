# Book Management API

A small FastAPI CRUD application for managing books.  
This project demonstrates CRUD operations using **FastAPI**, **SQLAlchemy**, and **SQLite**, along with **unit and integration testing**.

---

## Features

- Create, Read, Update, Delete books.
- Pagination and optional filtering by author.
- Proper response models using Pydantic.
- Basic error handling (404 for missing books).
- Unit test for business logic and integration tests for endpoints.

---

## Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- Pytest, FastAPI TestClient (for testing)

---

## Installation

1. Clone the repository:
```bash
git clone <repo_link>
cd CRUD_BOOK_API

Create a virtual environment:
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

Install dependencies:
pip install requirements.txt

Running the App
uvicorn main:app --reload
Open http://127.0.0.1:8000/docs to access the interactive Swagger UI.
Open http://127.0.0.1:8000/redoc for ReDoc docs.

API Endpoints
Method	Endpoint	Description
POST	/books/	    Create a new book
GET	    /books/	    List books (optional filter/pagination)
GET	    /books/{id}	Retrieve a book by ID
PUT	    /books/{id}	Update a book by ID
DELETE	/books/{id}	Delete a book by ID

Example Usage

Create Book
POST /books/
{
  "book_name": "1984",
  "author_name": "George Orwell"
}
Get All Books
GET /books/?limit=10&author=George Orwell

Get Single Book
GET /books/1

Update Book
PUT /books/1
{
  "book_name": "Animal Farm",
  "author_name": "George Orwell"
}

Delete Book
DELETE /books/1

Testing
Run all tests with:
pytest -v
test_logic.py → unit test for helper function
test_api.py → integration tests for CRUD endpoints