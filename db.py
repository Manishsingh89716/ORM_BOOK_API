"""database configuration using SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLite database URL
DATABASE_URL = "sqlite:///./books_test_crud.db"

#create SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base class for ORM models
Base = declarative_base()