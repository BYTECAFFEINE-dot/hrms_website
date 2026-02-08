"""
api/index.py
-----------
Entry point for Vercel serverless deployment.
This is the main FastAPI application.

Responsibilities:
✔ FastAPI app initialization
✔ Route handling (Employees + Attendance)
✔ Database session dependency
✔ Template rendering
✔ Form handling and validation
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pathlib import Path

from lib import models, schemas, crud
from lib.database import engine, SessionLocal, Base

# ---------------------------------------------------------
# DATABASE INITIALIZATION
# ---------------------------------------------------------

# Automatically creates database tables if they do not exist.
# In production projects this is usually handled by migrations.
Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------
# APP CONFIGURATION
# ---------------------------------------------------------

app = FastAPI(
    title="HRMS Lite",
    description="Lightweight HR Management System",
    version="1.0.0"
)

# Setup static files
base_dir = Path(__file__).parent.parent
static_dir = base_dir / "static"
templates_dir = base_dir / "templates"

if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

templates = Jinja2Templates(directory=str(templates_dir))


# ---------------------------------------------------------
# DATABASE DEPENDENCY
# ---------------------------------------------------------

def get_db():
    """
    Dependency that provides a database session
    for each request and ensures it closes properly.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================================================
# EMPLOYEE ROUTES
# =========================================================

@app.get("/", response_class=HTMLResponse)
def employees_page(request: Request, db: Session = Depends(get_db)):
    """
    Render Employees Page
    Shows all employees in the system.
    """
    employees = crud.get_employees(db)

    return templates.TemplateResponse(
        "employees.html",
        {
            "request": request,
            "employees": employees
        }
    )


@app.post("/employees")
def add_employee(
    employee_id: str = Form(...),
    full_name: str = Form(...),
    email: str = Form(...),
    department: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Add a new employee.
    Includes duplicate employee validation.
    """

    # Check for duplicate employee ID
    exists = db.query(models.Employee).filter(
        models.Employee.employee_id == employee_id
    ).first()

    if exists:
        raise HTTPException(
            status_code=400,
            detail="Employee already exists"
        )

    # Validate using Pydantic schema
    data = schemas.EmployeeCreate(
        employee_id=employee_id,
        full_name=full_name,
        email=email,
        department=department
    )

    crud.create_employee(db, data)

    # Redirect back to employee page
    return RedirectResponse("/", status_code=303)


@app.get("/delete/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    """
    Delete employee by database ID.
    """
    crud.delete_employee(db, emp_id)

    return RedirectResponse("/", status_code=303)


# =========================================================
# ATTENDANCE ROUTES
# =========================================================

@app.get("/attendance", response_class=HTMLResponse)
def attendance_page(request: Request, db: Session = Depends(get_db)):
    """
    Render Attendance Page.
    Shows attendance records and employee dropdown.
    """
    attendance = crud.get_attendance(db)
    employees = crud.get_employees(db)

    return templates.TemplateResponse(
        "attendance.html",
        {
            "request": request,
            "attendance": attendance,
            "employees": employees
        }
    )


@app.post("/attendance")
def mark_attendance(
    employee_id: str = Form(...),
    date: str = Form(...),
    status: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Mark attendance for an employee.
    """

    data = schemas.AttendanceCreate(
        employee_id=employee_id,
        date=date,
        status=status
    )

    crud.create_attendance(db, data)

    return RedirectResponse("/attendance", status_code=303)


# ---------------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------------

@app.get("/api/health")
def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {"status": "ok", "service": "hrms-lite"}
