"""
database.py
-----------
Handles database configuration and SQLAlchemy setup.

Responsibilities:
✔ Create database engine
✔ Manage session factory
✔ Provide Base model for ORM classes
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# ---------------------------------------------------------
# DATABASE CONFIGURATION
# ---------------------------------------------------------

# SQLite database path (stored in project root). Allow overriding with environment.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hrms.db")

# Create database engine
# check_same_thread=False is required for SQLite with FastAPI
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session factory used for dependency injection
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all ORM models
Base = declarative_base()
