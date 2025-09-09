"""schemas and ORM models"""
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, func
from datetime import datetime
from db import Base

#ORM model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, nullable=False)
    author_name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

#pydantic schemas
#schema for creating a book
class BookCreate(BaseModel):
    book_name: str
    author_name: str

#schema for updating a book
class BookUpdate(BaseModel):
    book_name: str
    author_name: str

#schema for returning book details
class BookResponse(BaseModel):
    id: int
    book_name: str
    author_name: str
    created_at: datetime

    class Config:
        orm_mode = True