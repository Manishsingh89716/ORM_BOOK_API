# Book Management API - Notes

## Architecture

- **FastAPI**: Web framework for building REST APIs.
- **SQLAlchemy ORM**: Object Relational Mapping for database interaction.
- **SQLite**: Lightweight file-based database.
- **Pydantic**: Data validation and response serialization.

---

## Approach

1. **Database Setup**
   - SQLite used for simplicity.
   - SQLAlchemy Base used for ORM mapping.
   - Tables auto-created on app startup.

2. **Models & Schemas**
   - `Book` ORM model: `id`, `book_name`, `author_name`, `created_at`.
   - Pydantic schemas: `BookCreate`, `BookUpdate`, `BookResponse`.
   - `created_at` auto-generated with timestamp.

3. **Endpoints**
   - CRUD operations all in `main.py`.
   - Dependency injection (`Depends`) for DB session.
   - Proper HTTP status codes and error handling (404).

4. **Custom Logic**
   - `format_book_description()` helper function demonstrates business logic separate from endpoints.

5. **Testing**
   - Unit test for helper function.
   - Integration tests using FastAPI TestClient to hit endpoints.
   - Tests cover create, read (list & single), pagination.

---

## Notes / Future Improvements

- Switch to PostgreSQL or MySQL for production.
- Add authentication/authorization.
- Add more advanced filtering and search.
- Migrate to SQLAlchemy 2.0 fully (deprecation warnings).
- Update Pydantic models for V2+ compatibility.

---

## Run Instructions (Summary)

1. Install dependencies.
2. Run `uvicorn main:app --reload`.
3. Open Swagger docs at `http://127.0.0.1:8000/docs`.
4. Run tests: `pytest -v`.