"""
main.py
-------
Main entry point for the HRMS Lite application.
This file wires together all components and runs the FastAPI server.

Can be run with:
    python main.py
    uvicorn main:app --reload
    uvicorn main:app --host 0.0.0.0 --port 8000
"""

import os
import sys
import uvicorn

# Add the project root to the Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the FastAPI application from api/index.py
from api.index import app

# Import database for initialization
from lib.database import engine, Base
from lib import models  # Import models to register them with Base

# ---------------------------------------------------------
# DATABASE INITIALIZATION
# ---------------------------------------------------------

# Create all database tables on startup
Base.metadata.create_all(bind=engine)

print("Database initialized")
print("FastAPI app loaded")


# ---------------------------------------------------------
# APPLICATION CONTEXT
# ---------------------------------------------------------

if __name__ == "__main__":
    """
    Entry point for running the server locally.
    
    Features:
    - Hot-reload enabled for development
    - Auto-discovery of routes
    - Automatic API documentation at /docs
    """
    
    # Configuration
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    reload = os.getenv("RELOAD", "true").lower() == "true"
    log_level = os.getenv("LOG_LEVEL", "info")
    
    print(f"\n{'='*60}")
    print("HRMS Lite - HR Management System")
    print(f"{'='*60}")
    print(f"Server: http://{host}:{port}")
    print(f"API Docs: http://{host}:{port}/docs")
    print(f"Reload: {'Enabled' if reload else 'Disabled'}")
    print(f"{'='*60}\n")
    
    # Run the Uvicorn server
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        log_level=log_level
    )
