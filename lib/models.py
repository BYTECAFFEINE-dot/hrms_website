"""
models.py
---------
Defines database ORM models using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .database import Base


class Employee(Base):
    """
    Employee Table
    Stores core employee information.
    """
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)


class Attendance(Base):
    """
    Attendance Table
    Stores daily attendance records.
    """
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, ForeignKey("employees.employee_id"))
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
