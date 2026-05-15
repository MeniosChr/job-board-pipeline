from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Board Data Pipeline API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/jobs", response_model=schemas.JobRead)
def create_job(job_in: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db, job_in)


@app.get("/jobs", response_model=list[schemas.JobRead])
def get_jobs(db: Session = Depends(get_db)):
    return crud.list_jobs(db)