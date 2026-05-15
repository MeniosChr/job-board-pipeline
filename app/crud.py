from sqlalchemy.orm import Session

from . import models, schemas


def get_job_by_title_company(db: Session, title: str, company: str) -> models.Job | None:
    return (
        db.query(models.Job)
        .filter(models.Job.title == title, models.Job.company == company)
        .first()
    )


def create_job(db: Session, job_in: schemas.JobCreate) -> models.Job:
    job = models.Job(
        title=job_in.title,
        company=job_in.company,
        description=job_in.description,
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def create_job_if_not_exists(db: Session, job_in: schemas.JobCreate) -> tuple[models.Job, bool]:
    existing = get_job_by_title_company(db, job_in.title, job_in.company)
    if existing:
        return existing, False
    created = create_job(db, job_in)
    return created, True


def list_jobs(db: Session) -> list[models.Job]:
    return db.query(models.Job).order_by(models.Job.created_at.desc()).all()