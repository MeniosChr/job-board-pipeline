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