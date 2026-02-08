"""
crud.py

This file contains all database interaction logic (CRUD operations).
Separating database logic from routes keeps the project modular,
clean, and easy to maintain.
"""

from sqlalchemy.orm import Session
from . import models, schemas


# ==========================================================
# EMPLOYEE OPERATIONS
# ==========================================================

def get_employees(db: Session):
    """
    Fetch all employees from the database.

    Args:
        db (Session): Active database session.

    Returns:
        List[Employee]: List of employee records.
    """
    return db.query(models.Employee).all()


def create_employee(db: Session, data: schemas.EmployeeCreate):
    """
    Create a new employee record.

    Steps:
    - Convert Pydantic schema into SQLAlchemy model
    - Add to session
    - Commit transaction
    - Refresh instance to get updated values (like ID)

    Args:
        db (Session): Database session
        data (EmployeeCreate): Employee input schema

    Returns:
        Employee: Newly created employee object
    """
    employee = models.Employee(**data.dict())

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def delete_employee(db: Session, emp_id: int):
    """
    Delete an employee by database ID.

    Args:
        db (Session): Database session
        emp_id (int): Employee primary key ID

    Returns:
        bool: True if deleted, False if not found
    """
    employee = (
        db.query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )

    if not employee:
        return False

    db.delete(employee)
    db.commit()
    return True


# ==========================================================
# ATTENDANCE OPERATIONS
# ==========================================================

def create_attendance(db: Session, data: schemas.AttendanceCreate):
    """
    Insert a new attendance record.

    Args:
        db (Session): Database session
        data (AttendanceCreate): Attendance input schema

    Returns:
        Attendance: Created attendance record
    """
    attendance = models.Attendance(**data.dict())

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return attendance


def get_attendance(db: Session):
    """
    Fetch all attendance records from the database.

    Args:
        db (Session): Active database session.

    Returns:
        List[Attendance]: List of attendance records.
    """
    return db.query(models.Attendance).all()
