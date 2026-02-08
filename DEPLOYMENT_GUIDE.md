# HRMS Lite - Vercel-Ready Deployment Guide

## 📁 New Project Structure

```
hrmslite_file/
├── api/                      # Vercel serverless functions
│   ├── __init__.py
│   └── index.py             # Main FastAPI app (Vercel entry point)
│
├── lib/                      # Shared application logic
│   ├── __init__.py
│   ├── database.py          # SQLAlchemy configuration
│   ├── models.py            # ORM models (Employee, Attendance)
│   ├── schemas.py           # Pydantic validation schemas
│   └── crud.py              # Database operations
│
├── static/                   # CSS, JS, images
│   └── style.css
│
├── templates/                # Jinja2 HTML templates
│   ├── base.html
│   ├── employees.html
│   └── attendance.html
│
├── vercel.json              # Vercel deployment configuration
├── .vercelignore            # Files to ignore during Vercel deployment
├── .gitignore               # Git ignore rules
├── .env.example             # Environment variables template
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## ✅ Can It Be Deployed on Vercel?

**YES!** Your FastAPI application is now configured for Vercel deployment.

### Supported Features:
- ✅ FastAPI web framework (fully supported on Vercel)
- ✅ SQLAlchemy ORM (works on Vercel)
- ✅ Jinja2 templates (supported)
- ✅ Static file serving (CSS, JS, images)
- ✅ Form handling and redirects (supported)

### Important Considerations:

#### Database Selection 🗄️
**SQLite (Current) ❌ NOT RECOMMENDED for Production**
- Vercel uses ephemeral filesystems - data will be lost after function invocation
- SQLite files stored locally won't persist between deployments

**Recommended Alternatives:**
1. **PostgreSQL** (Recommended) - Use Vercel's PostgreSQL or external services like Neon, Railway
2. **MongoDB** - Great for scalability
3. **MySQL** - Popular alternative to PostgreSQL

#### Migration Instructions:
```python
# For PostgreSQL (highly recommended):
DATABASE_URL = "postgresql://user:password@host:5432/database"

# For MySQL:
DATABASE_URL = "mysql+pymysql://user:password@host:3306/database"

# Add to requirements.txt:
# psycopg2-binary==2.9.9  (for PostgreSQL)
# pymysql==1.1.0          (for MySQL)
```

## 🚀 Deployment Steps

### Step 1: Prepare Your Repository
```bash
# Initialize git if not already done
git init
git add .
git commit -m "Initial commit: Vercel-ready structure"
```

### Step 2: Setup Environment Variables
Create a PostgreSQL database (recommended):
- Neon (https://neon.tech) - Free PostgreSQL tier
- Railway (https://railway.app)
- AWS RDS
- Vercel PostgreSQL (if available in your region)

### Step 3: Set Up Vercel
```bash
# Install Vercel CLI globally
npm install -g vercel

# Login to Vercel
vercel login

# Deploy from project directory
vercel
```

### Step 4: Configure Environment Variables in Vercel
In Vercel Dashboard:
1. Go to Project Settings → Environment Variables
2. Add `DATABASE_URL` with your PostgreSQL connection string
3. Example:
   ```
   DATABASE_URL=postgresql://user:password@host.neon.tech/dbname?sslmode=require
   ```

### Step 5: Deploy
```bash
# Redeploy after adding environment variables
vercel --prod
```

## 📋 Pre-Deployment Checklist

- [ ] Database switched from SQLite to PostgreSQL/MySQL
- [ ] `DATABASE_URL` environment variable configured in Vercel
- [ ] Updated `requirements.txt` with database driver (psycopg2/pymysql)
- [ ] `.env.example` created with template variables
- [ ] `vercel.json` configured correctly
- [ ] All code in `/api` and `/lib` folders
- [ ] Static files in `/static` folder
- [ ] Templates in `/templates` folder

## 🔧 Local Development

### Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create .env File
```bash
cp .env.example .env
# Edit .env and set DATABASE_URL if needed
```

### Run Locally
```bash
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

Visit: `http://localhost:8000`

## 📊 Performance Optimization for Vercel

1. **Database Connection Pooling:**
   - Use `SQLAlchemy` with connection pooling enabled ✅ (already configured)

2. **Request Timeout:**
   - Vercel has a 60-second timeout for serverless functions
   - Keep operations lean and quick

3. **Cold Starts:**
   - FastAPI initializes quickly
   - Database connections happen per-request (good for serverless)

4. **Static Files:**
   - Consider serving static files from Vercel's CDN
   - Currently mounted at `/static` ✅

## 🆘 Troubleshooting

### Issue: "Module not found" errors
**Solution:** Ensure all imports use the new structure:
```python
from lib import models, schemas, crud
from lib.database import engine, SessionLocal, Base
```

### Issue: Static files not loading
**Solution:** Vercel serves static files. Check:
- Static files are in `/static` directory
- `vercel.json` routes are configured

### Issue: Database connection timeout
**Solution:** 
- Verify `DATABASE_URL` is correct in Vercel environment
- Check database is accessible from Vercel servers
- For PostgreSQL, ensure SSL mode is enabled

### Issue: Deployment fails
**Solution:**
- Check logs: `vercel logs` in CLI
- Verify `requirements.txt` has all dependencies
- Ensure Python version compatibility (Python 3.8+)

## 📚 Additional Resources

- [Vercel Python Documentation](https://vercel.com/docs/concepts/functions/serverless-functions/python)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Neon PostgreSQL Setup](https://neon.tech/docs)

## 📝 Next Steps

1. **Choose a database provider** (PostgreSQL recommended)
2. **Update `requirements.txt`** with database driver
3. **Test locally** with the new structure
4. **Push to GitHub**
5. **Connect GitHub to Vercel**
6. **Add environment variables** in Vercel Dashboard
7. **Deploy!** 🚀

---

**Note:** The original `main.py`, `models.py`, `schemas.py`, `crud.py`, and `database.py` in the root directory can be safely deleted once you verify everything works with the new structure in `/api` and `/lib`.
