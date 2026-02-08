#!/bin/bash
# Deployment Verification Script
# Run this before deploying to Vercel

echo "🔍 HRMS Lite Deployment Verification"
echo "===================================="
echo ""

# Check Python version
echo "✓ Python Version:"
python --version
echo ""

# Check required files exist
echo "✓ Required Files:"
files=("requirements.txt" "vercel.json" "api/index.py" "lib/database.py" ".env")
for file in "${files[@]}"; do
  if [ -f "$file" ]; then
    echo "  ✅ $file"
  else
    echo "  ❌ $file (MISSING!)"
  fi
done
echo ""

# Check dependencies
echo "✓ Installing Dependencies:"
pip install -q -r requirements.txt
if [ $? -eq 0 ]; then
  echo "  ✅ All dependencies installed"
else
  echo "  ❌ Dependency installation failed"
  exit 1
fi
echo ""

# Check database connection
echo "✓ Database Connection Test:"
python -c "
import os
from lib.database import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(text('SELECT 1'))
        print('  ✅ PostgreSQL connection successful')
except Exception as e:
    print(f'  ❌ Database connection failed: {e}')
    exit(1)
"
echo ""

# Verify FastAPI imports
echo "✓ FastAPI Application:"
python -c "
from api.index import app
print(f'  ✅ FastAPI app loaded successfully')
print(f'  📱 Routes: {len([r for r in app.routes])} total')
"
echo ""

echo "===================================="
echo "✅ All checks passed! Ready to deploy to Vercel"
echo ""
echo "Next steps:"
echo "1. git push origin main"
echo "2. Vercel will auto-deploy on push"
echo "3. Set DATABASE_URL in Vercel environment variables"
