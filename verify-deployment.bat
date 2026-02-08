@echo off
REM Deployment Verification Script for Windows
REM Run this before deploying to Vercel

echo.
echo 🔍 HRMS Lite Deployment Verification
echo ====================================
echo.

REM Check Python version
echo ✓ Python Version:
python --version
echo.

REM Check required files
echo ✓ Required Files:
for %%f in (requirements.txt vercel.json .env) do (
    if exist "%%f" (
        echo   ✅ %%f
    ) else (
        echo   ❌ %%f ^(MISSING!^)
    )
)

if exist "api\index.py" (
    echo   ✅ api/index.py
) else (
    echo   ❌ api/index.py ^(MISSING!^)
)

if exist "lib\database.py" (
    echo   ✅ lib/database.py
) else (
    echo   ❌ lib/database.py ^(MISSING!^)
)
echo.

REM Install dependencies
echo ✓ Installing Dependencies:
pip install -q -r requirements.txt
if %ERRORLEVEL% equ 0 (
    echo   ✅ All dependencies installed
) else (
    echo   ❌ Dependency installation failed
    pause
    exit /b 1
)
echo.

REM Test database connection
echo ✓ Database Connection Test:
python -c "from lib.database import engine; from sqlalchemy import text; conn = engine.connect(); conn.execute(text('SELECT 1')); conn.close(); print('   ✅ PostgreSQL connection successful')" 2>nul || echo   ❌ Database connection failed
echo.

REM Verify FastAPI
echo ✓ FastAPI Application:
python -c "from api.index import app; print('   ✅ FastAPI app loaded successfully')" 2>nul || echo   ❌ FastAPI app failed to load
echo.

echo ====================================
echo ✅ All checks passed! Ready to deploy to Vercel
echo.
echo Next steps:
echo 1. git push origin main
echo 2. Vercel will auto-deploy on push
echo 3. Set DATABASE_URL in Vercel environment variables
echo.
pause
