# 🐘 PostgreSQL Setup Guide

Your project is now configured for **PostgreSQL**. Here's how to set it up.

## 📋 Option 1: Local PostgreSQL Setup (For Development)

### Windows

#### 1. Download & Install PostgreSQL
- Download from: https://www.postgresql.org/download/windows/
- Install with default settings
- Remember the **postgres** password you set during installation

#### 2. Verify Installation
Open PowerShell and run:
```powershell
psql --version
```
You should see: `psql (PostgreSQL) 15.x` or similar

#### 3. Create Database
```powershell
# Connect to PostgreSQL with default user 'postgres'
psql -U postgres

# You'll see the psql prompt: postgres=#
# Now create your HRMS database:
CREATE DATABASE hrms_db;

# Verify it was created:
\l

# Exit psql:
\q
```

#### 4. Update .env File
Edit `.env` file in your project root:
```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/hrms_db
```

Replace `YOUR_PASSWORD` with the postgres password you set during installation.

#### 5. Install Python Packages
```powershell
pip install -r requirements.txt
```

#### 6. Run Locally
```powershell
python -m uvicorn api.index:app --reload
```

Visit: `http://localhost:8000`

---

### macOS

```bash
# Install PostgreSQL with Homebrew
brew install postgresql@15

# Start PostgreSQL service
brew services start postgresql@15

# Create database
createdb hrms_db

# Update .env (same as Windows)
# DATABASE_URL=postgresql://username:password@localhost:5432/hrms_db

# Run locally
pip install -r requirements.txt
python -m uvicorn api.index:app --reload
```

---

### Linux (Ubuntu/Debian)

```bash
# Install PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL
sudo systemctl start postgresql

# Switch to postgres user and create database
sudo -u postgres createdb hrms_db

# Create a user (optional but recommended)
sudo -u postgres createuser hrms_user

# Set password
sudo -u postgres psql -c "ALTER USER hrms_user WITH PASSWORD 'your_password';"

# Grant privileges
sudo -u postgres psql -d hrms_db -c "GRANT ALL PRIVILEGES ON DATABASE hrms_db TO hrms_user;"

# Update .env
# DATABASE_URL=postgresql://hrms_user:your_password@localhost:5432/hrms_db

# Run locally
pip install -r requirements.txt
python -m uvicorn api.index:app --reload
```

---

## 🚀 Option 2: Cloud PostgreSQL (For Vercel Deployment)

### Using Neon (RECOMMENDED - Free Tier)

Neon provides a free PostgreSQL database perfect for Vercel deployment.

#### Step 1: Create Neon Account
1. Go to: https://neon.tech
2. Click "Sign Up"
3. Sign in with GitHub (recommended)

#### Step 2: Create Database
1. Click "Create Project"
2. Name: `hrms-lite` (or anything you want)
3. Select Region closest to you
4. Click "Create Project"

#### Step 3: Get Connection String
1. You'll see a connection string like:
   ```
   postgresql://user:randompass@ep-xxx.neon.tech/dbname?sslmode=require
   ```
2. Copy this entire string

#### Step 4: Test Locally (Optional)
Update `.env`:
```env
DATABASE_URL=postgresql://user:randompass@ep-xxx.neon.tech/dbname?sslmode=require
```

Run:
```bash
pip install -r requirements.txt
python -m uvicorn api.index:app --reload
```

#### Step 5: Deploy to Vercel
1. Push your code to GitHub
2. Go to: https://vercel.com
3. Click "Import Project"
4. Select your GitHub repository
5. Add Environment Variables:
   - Key: `DATABASE_URL`
   - Value: Your Neon connection string (from Step 3)
6. Click "Deploy"

---

### Alternative Cloud Options

#### Railway (https://railway.app)
```bash
# After creating a PostgreSQL instance on Railway:
DATABASE_URL=postgresql://user:password@containers-us-west-123.railway.app:5432/railway
```

#### AWS RDS
```bash
DATABASE_URL=postgresql://user:password@hrms.xxxxx.us-east-1.rds.amazonaws.com:5432/hrmsdb
```

#### Vercel Postgres (Enterprise)
```bash
# Available if you have Vercel Pro
DATABASE_URL=postgres://user:password@aws-0-us-east-1.sql.vercel-postgres.com/dbname
```

---

## ✅ Verify PostgreSQL Connection

### Test Connection Locally

```python
# Create a test file: test_db.py
from lib.database import engine, Base
from sqlalchemy import text

# Try to connect
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        print(result.fetchone())
        print("✅ PostgreSQL connection successful!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

Run:
```bash
python test_db.py
```

You should see something like:
```
('PostgreSQL 15.x on x86_64-pc-linux-gnu, compiled by gcc ...',)
✅ PostgreSQL connection successful!
```

---

## 🔧 Database Operations

### Create Tables Automatically
Tables are created automatically when you run the app:
```bash
python -m uvicorn api.index:app --reload
```

### Access Database with psql (Local)

```bash
# Connect to your database
psql -U postgres -d hrms_db

# List tables
\dt

# Query employees
SELECT * FROM employees;

# Query attendance
SELECT * FROM attendance;

# Exit
\q
```

### Access Database with pgAdmin (GUI)

pgAdmin is a web-based PostgreSQL management tool:

**Windows/macOS:**
```bash
pip install pgadmin4
pgadmin4
```

Then open: `http://localhost:5050`

**Or use online:** https://www.pgadmin.org/

---

## 📊 Connection String Examples

```
# Local PostgreSQL
postgresql://postgres:password@localhost:5432/hrms_db

# Neon (Vercel-ready)
postgresql://user:randomPass123@ep-silent-lake-123456.us-east-1.neon.tech/hrms_db?sslmode=require

# Railway
postgresql://user:password@containers-us-west-456.railway.app:5432/railway

# AWS RDS
postgresql://admin:password@hrms-db.123456.us-east-1.rds.amazonaws.com:5432/hrmsdb

# Azure Database for PostgreSQL
postgresql://adminuser@servername:password@servername.postgres.database.azure.com:5432/hrmsdb
```

---

## 🐛 Troubleshooting

### Error: "connection refused"
- PostgreSQL is not running
- **Solution:** Start PostgreSQL service
  ```bash
  # Windows/PowerShell:
  pg_ctl -D "C:\Program Files\PostgreSQL\15\data" start
  
  # macOS:
  brew services start postgresql@15
  
  # Linux:
  sudo systemctl start postgresql
  ```

### Error: "FATAL: Ident authentication failed"
- Wrong user or password
- **Solution:** Check `.env` DATABASE_URL is correct

### Error: "database does not exist"
- Database hasn't been created
- **Solution:** Create it with `createdb hrms_db`

### Error: "SSL error" on Neon
- SSL mode mismatch
- **Solution:** Ensure connection string has `?sslmode=require`

---

## 🎯 Quick Start Summary

**For Local Development:**
```bash
# 1. Create database
createdb hrms_db

# 2. Update .env
# DATABASE_URL=postgresql://postgres:password@localhost:5432/hrms_db

# 3. Install & Run
pip install -r requirements.txt
python -m uvicorn api.index:app --reload
```

**For Vercel Deployment:**
```bash
# 1. Create Neon database (https://neon.tech)
# 2. Copy connection string
# 3. Add to Vercel environment variables
# 4. Deploy!
```

---

## 📚 Useful PostgreSQL Commands

```sql
-- List all databases
\l

-- Connect to database
\c hrms_db

-- List all tables
\dt

-- Show table structure
\d employees

-- Insert test data
INSERT INTO employees (employee_id, full_name, email, department) 
VALUES ('EMP001', 'John Doe', 'john@example.com', 'IT');

-- Query data
SELECT * FROM employees;
SELECT * FROM attendance;

-- Delete database (careful!)
DROP DATABASE hrms_db;

-- Exit psql
\q
```

---

You're now ready to use PostgreSQL! 🎉

**Next Steps:**
1. Choose: Local PostgreSQL or Neon Cloud
2. Set up your database
3. Update `.env` with connection string
4. Test with `python -m uvicorn api.index:app --reload`
5. Deploy to Vercel when ready!
