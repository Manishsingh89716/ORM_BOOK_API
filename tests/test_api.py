"""integration tests for FastAPI endpoints"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_book():
    """test creating a book and then retrieving it"""
    #create
    response = client.post(
        "/books/",
        json={"book_name": "1984", "author_name": "George Orwell"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["book_name"] == "1984"
    assert data["author_name"] == "George Orwell"
    book_id = data["id"]

    #fetch same book
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    assert data["book_name"] == "1984"
    assert data["author_name"] == "George Orwell"

def test_get_books_list():
    """test fetching list of books"""
    response = client.get("/books/?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0