from pydantic import BaseModel, Field
from app.domain import UserProgress

from datetime import datetime, timezone

class TaskCreate(BaseModel): 
    id: int = Field(description="this is a unique id for a task")
    project_id: int
    title: str = Field(min_length=5, max_length=50)
    description: str | None = None
    status: UserProgress | None = None
    created_at: datetime.now(timezone.utc)

class TaskUpdate(BaseModel): 
    title: str | None = None
    description: str | None = None
    status: UserProgress | None = None
    updated_at: datetime.now(timezone.utc)

class TaskRead(BaseModel): 
    title: str | None = None
    description: str | None = None
    status: UserProgress | None = None
    








