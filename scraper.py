import httpx
from bs4 import BeautifulSoup

from app import models, schemas
from app.crud import create_job_if_not_exists
from app.db import SessionLocal, engine

FAKE_JOBS_URL = "https://realpython.github.io/fake-jobs/"


def scrape_jobs():
    response = httpx.get(FAKE_JOBS_URL, timeout=20.0)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    cards = soup.select("div.card-content")

    jobs = []
    for card in cards:
        title_el = card.select_one("h2.title")
        company_el = card.select_one("h3.company")
        content_el = card.select_one("div.content")

        if not title_el or not company_el:
            continue

        title = title_el.get_text(strip=True)
        company = company_el.get_text(strip=True)
        description = (
            content_el.get_text(" ", strip=True)
            if content_el
            else "No description from source."
        )

        jobs.append(
            schemas.JobCreate(
                title=title,
                company=company,
                description=description,
            )
        )

    return jobs


def main():
    # Ensures table exists if script runs before API startup
    models.Base.metadata.create_all(bind=engine)

    jobs = scrape_jobs()
    db = SessionLocal()
    inserted = 0
    skipped = 0

    try:
        for job_in in jobs:
            _, created = create_job_if_not_exists(db, job_in)
            if created:
                inserted += 1
            else:
                skipped += 1
    finally:
        db.close()
    print(f"Inserted {inserted} jobs, skipped {skipped} duplicates.")


if __name__ == "__main__":
    main()