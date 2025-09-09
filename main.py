from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
import db, schemas

#create database tables
db.Base.metadata.create_all(bind=db.engine)
app = FastAPI(title="Book Management API")

#dependency to get DB session
def get_db():
    """provide a database session"""
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()

#book creation endpoint
@app.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, session: Session = Depends(get_db)):
    """create a new book"""
    new_book = schemas.Book(**book.dict())
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book

#read all the book by get endpoint
@app.get("/books/", response_model=List[schemas.BookResponse])
def get_books(
    limit: int = 10,
    offset: int = 0,
    author: Optional[str] = None,
    session: Session = Depends(get_db),
):
    """get all books (with optional filter & pagination)"""
    query = session.query(schemas.Book)
    if author:
        query = query.filter(schemas.Book.author_name == author)
    return query.offset(offset).limit(limit).all()

#endpoint for get by id
@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, session: Session = Depends(get_db)):
    """get a book by ID"""
    book = session.query(schemas.Book).filter(schemas.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

#endpoint for update book by id
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, session: Session = Depends(get_db)):
    """update a book"""
    db_book = session.query(schemas.Book).filter(schemas.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_book.book_name = book.book_name
    db_book.author_name = book.author_name
    session.commit()
    session.refresh(db_book)
    return db_book

#endpoint for delete the book by id
@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_db)):
    """delete a book"""
    book = session.query(schemas.Book).filter(schemas.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)
    session.commit()
    return {"message": "Book deleted successfully"}

#testing part
def format_book_description(book_name: str, author_name: str) -> str:
    """return a formatted description of a book"""
    return f"{book_name} is written by {author_name}"