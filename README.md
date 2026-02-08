# HRMS Lite - Lightweight HR Management System

A lightweight, easy-to-use HR Management System built with **FastAPI**, **SQLAlchemy**, and **SQLite**. Manage employees and track attendance with a simple and intuitive web interface.

## 📋 Features

- **Employee Management**: Create, read, update, and delete employee records
- **Attendance Tracking**: Record and manage daily attendance for employees
- **Web Interface**: Clean and responsive UI using Jinja2 templates
- **RESTful API**: Built with FastAPI for easy integration
- **SQLite Database**: No setup required, data stored locally

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository** (or extract the project)
   ```bash
   cd hrmslite_file
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional)
   ```bash
   # Copy .env.example to .env and update values if needed
   copy .env.example .env
   ```

### Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The application will be available at:
- **Web UI**: http://localhost:8000/
- **API Docs**: http://localhost:8000/docs (Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc (ReDoc)

## 📁 Project Structure

```
hrmslite_file/
├── main.py              # FastAPI app and routes
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic validation schemas
├── crud.py              # Create, Read, Update, Delete operations
├── database.py          # Database configuration and setup
├── requirements.txt     # Python dependencies
├── .env                 # Local environment variables (git-ignored)
├── .env.example         # Example environment template
├── .gitignore           # Git ignore rules
├── static/              # CSS, JS, and static assets
│   └── style.css        # Application styles
├── templates/           # HTML templates
│   ├── base.html        # Base template layout
│   ├── employees.html   # Employee management page
│   └── attendance.html  # Attendance tracking page
└── README.md            # This file
```

## 💾 Database

The application uses **SQLite** for data storage. The database file (`hrms.db`) is created automatically on first run.

### Database Schema

#### Employees Table
- `id` - Primary key (auto-increment)
- `employee_id` - Unique employee identifier
- `full_name` - Employee's full name
- `email` - Email address (unique)
- `department` - Department name

#### Attendance Table
- `id` - Primary key (auto-increment)
- `employee_id` - Foreign key to employees
- `date` - Attendance date
- `status` - Attendance status (Present, Absent, Leave, etc.)

## 🔧 Configuration

### Environment Variables

The application supports the following environment variables (see `.env.example`):

- `SECRET_KEY` - Secret key for session management
- `DATABASE_URL` - Database connection string (default: `sqlite:///./hrms.db`)
- `DEBUG` - Debug mode (default: `True`)
- `EMAIL_USER` - Email user for notifications (optional)
- `EMAIL_PASSWORD` - Email password for notifications (optional)

## 📦 Dependencies

- **fastapi** - Modern Python web framework
- **uvicorn** - ASGI server for running FastAPI
- **sqlalchemy** - SQL toolkit and ORM
- **jinja2** - Template engine for HTML rendering
- **python-multipart** - Form data parsing
- **email-validator** - Email validation

See `requirements.txt` for exact versions.

## 🛣️ API Routes

### Employees
- `GET /` - Home page / employee list
- `POST /add-employee` - Add new employee
- `POST /edit-employee/{employee_id}` - Update employee
- `POST /delete-employee/{employee_id}` - Delete employee

### Attendance
- `GET /attendance` - Attendance tracking page
- `POST /record-attendance` - Record attendance for employee
- `POST /update-attendance/{record_id}` - Update attendance record

## 🔐 Security Notes

⚠️ **Before pushing to production or public GitHub:**

1. Change the `SECRET_KEY` in `.env` to a secure random value
2. Never commit `.env` file (already in `.gitignore`)
3. For production, consider using a real database like PostgreSQL
4. Enable HTTPS/SSL in production
5. Add authentication/authorization if handling sensitive data
6. Review and update CORS settings in `main.py` if needed

## 📝 Development Tips

- **Database Migrations**: For production, consider using Alembic for schema management
- **Testing**: Add unit tests using pytest
- **Logging**: Implement proper logging for debugging
- **Validation**: Extend Pydantic schemas for more robust validation
- **Error Handling**: Add comprehensive error handling and user feedback

## 🐛 Troubleshooting

### Application won't start
- Ensure Python 3.8+ is installed
- Check that all dependencies in `requirements.txt` are installed
- Verify the port 8000 is not in use

### Database errors
- Delete `hrms.db` to reset the database
- Check file permissions in the project directory
- Ensure `DATABASE_URL` in `.env` is correctly formatted

### Static files not loading
- Verify the `static/` directory exists
- Check the `style.css` file is present
- Clear browser cache and restart the server

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

HRMS Lite - Lightweight HR Management System

---

**Last Updated**: February 2026

For issues, suggestions, or contributions, feel free to reach out!
