from fastapi import FastAPI
from typing import List

from .models import Job, JobCreate
from .storage import JobStorage

app = FastAPI(title="ComputeHub API")

storage = JobStorage()


@app.post("/jobs", response_model=Job)
def create_job(job: JobCreate):
    return storage.create_job(job)


@app.get("/jobs", response_model=List[Job])
def list_jobs():
    return storage.list_jobs()
