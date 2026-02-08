#!/usr/bin/env python3
"""
Deployment Verification Script
Checks if the application is ready for Vercel deployment
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath: str) -> bool:
    """Check if a file exists"""
    return Path(filepath).exists()

def check_python_modules():
    """Check if required Python modules are importable"""
    modules = [
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "jinja2",
        "pydantic",
        "dotenv"
    ]
    
    print("✓ Checking Python Modules:")
    all_ok = True
    for module in modules:
        try:
            __import__(module)
            print(f"  ✅ {module}")
        except ImportError:
            print(f"  ❌ {module} (not installed)")
            all_ok = False
    
    return all_ok

def check_database_connection():
    """Test database connection"""
    print("\n✓ Database Connection Test:")
    try:
        from lib.database import engine
        from sqlalchemy import text
        
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("  ✅ PostgreSQL connection successful")
            return True
    except Exception as e:
        print(f"  ❌ Database connection failed: {e}")
        return False

def check_fastapi_app():
    """Check if FastAPI app loads"""
    print("\n✓ FastAPI Application:")
    try:
        from api.index import app
        route_count = len([r for r in app.routes])
        print(f"  ✅ FastAPI app loaded successfully")
        print(f"  📱 Routes: {route_count} total")
        return True
    except Exception as e:
        print(f"  ❌ FastAPI app failed to load: {e}")
        return False

def main():
    """Run all checks"""
    print("\n🚀 HRMS Lite - Deployment Verification\n")
    print("=" * 50)
    
    # Check critical files
    print("\n✓ Critical Files:")
    required_files = {
        "requirements.txt": "Dependency list",
        "vercel.json": "Vercel config",
        "api/index.py": "FastAPI entry point",
        "lib/database.py": "Database config",
        "lib/models.py": "SQLAlchemy models",
        "lib/schemas.py": "Pydantic schemas",
        "lib/crud.py": "Database operations",
    }
    
    all_files_ok = True
    for filepath, description in required_files.items():
        if check_file_exists(filepath):
            print(f"  ✅ {filepath} ({description})")
        else:
            print(f"  ❌ {filepath} (MISSING!)")
            all_files_ok = False
    
    if not all_files_ok:
        print("\n❌ Some required files are missing!")
        return False
    
    # Check Python version
    print("\n✓ Python Version:")
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    if sys.version_info.major == 3 and sys.version_info.minor >= 8:
        print(f"  ✅ {py_version} (compatible)")
    else:
        print(f"  ❌ {py_version} (requires 3.8+)")
        return False
    
    # Check modules
    if not check_python_modules():
        print("\n⚠️  Install dependencies: pip install -r requirements.txt")
        return False
    
    # Check database
    if not check_database_connection():
        print("\n⚠️  Check DATABASE_URL environment variable")
        return False
    
    # Check FastAPI
    if not check_fastapi_app():
        return False
    
    # Summary
    print("\n" + "=" * 50)
    print("✅ All checks passed! Ready for Vercel deployment\n")
    print("Next steps:")
    print("1. git push origin main")
    print("2. Vercel auto-deploys on push")
    print("3. Add DATABASE_URL to Vercel environment variables")
    print("4. Your app will be live!\n")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
