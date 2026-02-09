Deploying to Render
===================

Quick steps:

1. Create a new Web Service on Render and connect your repository.
2. Choose "Python" as the environment.
3. Use the build command: `pip install -r requirements.txt`.
4. Use the start command: `gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT`.
5. Set the `DATABASE_URL` environment variable on Render if you want to use Postgres.

Notes:
- The repo contains a `render.yaml` manifest and a `Procfile` for convenience.
- By default the app uses SQLite (`sqlite:///./hrms.db`) when `DATABASE_URL` is not set.
- If you encounter encoding problems in logs, enable UTF-8 by setting `PYTHONIOENCODING=utf-8`.
