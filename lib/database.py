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
from sqlalchemy.pool import NullPool

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# ---------------------------------------------------------
# DATABASE CONFIGURATION
# ---------------------------------------------------------

# Database URL with environment override support
# PostgreSQL format (recommended for production):
#   postgresql://user:password@host:5432/database
# For local development with SQLite (fallback):
#   sqlite:///./hrms.db
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hrms.db")

# Create database engine with appropriate settings
if "postgresql" in DATABASE_URL:
    # PostgreSQL configuration (for production/Vercel)
    engine = create_engine(
        DATABASE_URL,
        poolclass=NullPool,  # Better for serverless/Vercel
        echo=False
    )
else:
    # SQLite configuration (for local development)
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
