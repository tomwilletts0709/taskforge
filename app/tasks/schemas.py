from datetime import datetime

from pydantic import BaseModel, Field

from app.domain import TaskStatus

class TaskCreate(BaseModel): 
    project_id: int
    title: str = Field(min_length=5, max_length=50)
    description: str | None = None

class TaskUpdate(BaseModel): 
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None

class TaskRead(BaseModel): 
    id: int
    project_id: int
    title: str
    description: str | None = None
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
