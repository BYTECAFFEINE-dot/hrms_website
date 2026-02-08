# Files to Archive or Delete

After verifying the new structure works properly, you can safely delete or archive these old files:

## ✓ Safe to Delete (After Testing)
- `main.py` - Moved to `api/index.py`
- `models.py` - Moved to `lib/models.py`
- `schemas.py` - Moved to `lib/schemas.py`
- `crud.py` - Moved to `lib/crud.py`
- `database.py` - Moved to `lib/database.py`

## Verification Steps Before Deletion:

1. **Test locally:**
   ```bash
   pip install -r requirements.txt
   uvicorn api.index:app --reload
   ```

2. **Verify all routes work:**
   - Visit `http://localhost:8000/` (employees page)
   - Visit `http://localhost:8000/attendance` (attendance page)
   - Test adding/deleting employees
   - Test marking attendance

3. **Test with Vercel CLI:**
   ```bash
   vercel dev
   ```

4. **Only after everything works**, run:
   ```bash
   rm main.py models.py schemas.py crud.py database.py
   ```

## Archive Instead of Delete:
If you prefer to keep backups:
```bash
mkdir old_structure_backup
mv main.py models.py schemas.py crud.py database.py old_structure_backup/
```

This way you have a backup if something goes wrong!
