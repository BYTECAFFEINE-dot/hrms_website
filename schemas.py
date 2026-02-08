"""
schemas.py
----------
Pydantic schemas used for validation and data transfer.
"""

from pydantic import BaseModel, EmailStr
from datetime import date


class EmployeeCreate(BaseModel):
    """
    Schema for creating an employee.
    """
    employee_id: str
    full_name: str
    email: EmailStr
    department: str


class AttendanceCreate(BaseModel):
    """
    Schema for creating attendance.
    """
    employee_id: str
    date: date
    status: str
