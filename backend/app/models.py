from enum import Enum
from pydantic import BaseModel
from typing import Optional


class JobStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class JobCreate(BaseModel):
    name: str
    job_type: str


class Job(JobCreate):
    id: int
    status: JobStatus
    result: Optional[str] = None
