from typing import List
from .models import Job, JobCreate, JobStatus


class JobStorage:
    def __init__(self):
        self.jobs: List[Job] = []
        self.counter = 1

    def create_job(self, data: JobCreate) -> Job:
        job = Job(
            id=self.counter,
            name=data.name,
            job_type=data.job_type,
            status=JobStatus.PENDING,
        )
        self.counter += 1
        self.jobs.append(job)
        return job

    def list_jobs(self) -> List[Job]:
        return self.jobs
