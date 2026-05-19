# Job Board Data Pipeline

A production-style backend project built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, and **Docker**.

This project exposes a REST API for job records and includes a standalone ingestion pipeline (`scraper.py`) that scrapes job data from a test source and inserts it into the database.

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Docker + Docker Compose
- httpx + BeautifulSoup4 + lxml

## Features

- Create and list jobs via REST API
- SQLAlchemy ORM model for `jobs`
- Dockerized API service
- Dockerized PostgreSQL database
- Env-based DB configuration (`DATABASE_URL`)
- Standalone scraper pipeline
- Idempotent ingestion logic (skip duplicates by title + company)

## Project Structure
```text
job-board-pipeline/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ db.py
│  ├─ models.py
│  ├─ schemas.py
│  └─ crud.py
├─ scraper.py
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ .dockerignore
└─ README.md
```
## API Endpoints
POST /jobs
Create a job record.

Example request body:
```
{
  "title": "Backend Engineer",
  "company": "Acme",
  "description": "Build ETL services"
}
```

`GET /jobs`
Return all jobs ordered by newest first.

# Run Locally (without Docker)
```
python -m venv .venv

# Windows

.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

# Run with Docker (API + Postgres)
`docker compose up --build`

API docs:

http://127.0.0.1:8000/docs

##Run Scraper Pipeline

Local Python environment
`python scraper.py`

Inside Docker API container
`docker compose exec api python scraper.py`

Expected output:
`Inserted X jobs, skipped Y duplicates.`

## Environment Variables
app/db.py uses:

DATABASE_URL (optional)
default: sqlite:///./jobs.db
docker-compose sets: postgresql+psycopg2://jobuser:jobpass@db:5432/jobsdb

Then commit:
```bash
git add README.md
git commit -m "Polish README markdown formatting"
git push
