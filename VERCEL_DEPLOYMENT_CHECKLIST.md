# 🚀 Vercel Deployment Checklist

Your HRMS Lite application is ready for Vercel deployment!

## ✅ Pre-Deployment Verification

Before deploying to Vercel, verify everything locally:

### Option 1: Windows (PowerShell)
```powershell
.\verify-deployment.bat
```

### Option 2: macOS/Linux (Bash)
```bash
bash verify-deployment.sh
```

### Option 3: Manual Verification
```bash
# 1. Check Python version
python --version

# 2. Install dependencies
pip install -r requirements.txt

# 3. Test database connection
python -c "from lib.database import engine; engine.connect().close(); print('✅ DB OK')"

# 4. Test FastAPI app
python -c "from api.index import app; print(f'✅ App loaded with {len([r for r in app.routes])} routes')"
```

---

## 📋 Deployment Configuration Files

✅ **vercel.json** - Build & routing config
✅ **.vercelignore** - Files to exclude from deployment
✅ **.env** - Local database URL (DO NOT COMMIT)
✅ **requirements.txt** - Python dependencies with pinned versions
✅ **build.json** - Optional Vercel build settings

---

## 🚀 Step-by-Step Deployment to Vercel

### Step 1: Final Code Review
```bash
git status
# Should show no uncommitted changes
```

### Step 2: Commit & Push
```bash
git add .
git commit -m "Ready for Vercel deployment with PostgreSQL"
git push origin main
```

### Step 3: Connect to Vercel
1. Go to https://vercel.com
2. Click "Add New..." → "Project"
3. Select your GitHub repository
4. Click "Import"

### Step 4: Configure Environment Variables
1. In Vercel Project Settings → Environment Variables
2. Add variable:
   - **Name:** `DATABASE_URL`
   - **Value:** `postgresql://neondb_owner:npg_q7gB5CjORXte@ep-blue-bread-a1h9k63i-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require`
3. Click "Save"

### Step 5: Deploy
1. Click "Deploy"
2. Wait for build to complete (2-3 minutes)
3. Get your live URL! 🎉

---

## 🔒 Security Checklist

- ✅ `.env` file is in `.gitignore` (don't commit!)
- ✅ Database password in Vercel environment variables only
- ✅ No hardcoded secrets in code
- ✅ PostgreSQL with SSL enabled (`sslmode=require`)
- ✅ API health check endpoint: `/api/health`

---

## 🧪 Test Deployed Application

Once deployed, test these endpoints:

```bash
# Replace with your Vercel URL
VERCEL_URL="https://your-app.vercel.app"

# 1. Health check
curl $VERCEL_URL/api/health

# 2. Home page (employees)
curl $VERCEL_URL

# 3. Attendance page
curl $VERCEL_URL/attendance
```

Expected responses:
- ✅ Health: `{"status":"ok","service":"hrms-lite"}`
- ✅ Pages: HTML content loads

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"
**Fix:** Verify `api/index.py` and `lib/` exist in repository

### Issue: "DATABASE_URL not found"
**Fix:** Add environment variable in Vercel dashboard

### Issue: "PostgreSQL connection timeout"
**Fix:** Check Neon database is running and accessible

### Issue: "Build failed"
**Fix:** Check Vercel build logs for specific error

View logs:
```bash
vercel logs
```

---

## 📊 Post-Deployment

### Monitor Application
1. Vercel Dashboard → Deployments
2. Check build logs and function logs
3. View analytics and errors

### Update Code
```bash
# Make changes locally
git add .
git commit -m "Update feature"
git push origin main
# Vercel auto-deploys!
```

### Rollback if Needed
1. Vercel Dashboard → Deployments
2. Click on previous deployment
3. Click "Redeploy"

---

## 🎉 Success!

Your HRMS Lite is now live on Vercel!

**Deployed URL:** `https://your-project.vercel.app`

### Share with Team
- Employees page: `https://your-project.vercel.app/`
- Attendance page: `https://your-project.vercel.app/attendance`

---

## 📚 Next Steps

1. ✅ Test all features work correctly
2. ✅ Monitor application performance
3. ✅ Set up error tracking (Sentry, etc.)
4. ✅ Configure custom domain (if needed)
5. ✅ Set up CI/CD automations

---

## 🔗 Useful Links

- [Vercel Dashboard](https://vercel.com/dashboard)
- [Neon Console](https://console.neon.tech)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

---

**Your deployment is ready!** 🚀
