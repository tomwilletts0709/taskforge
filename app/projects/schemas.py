from typing import Optional
from pydantic import BaseModel, Field, model_validator
from app.domain import TaskStatus

class CreateProject(BaseModel): 
    title: str = Field(min_length=5, max_length=50)
    description: str = Field(min_length=10, max_length=250)
    

class UpdateProject(BaseModel):
    title: Optional[str] = Field(min_length=5, max_length=50)
    description: Optional[str] = Field(min_length=10, max_length=250)
    status: Optional[TaskStatus]
    

class ReadProject(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=50)
    description: str = Field(min_length=10, max_length=250)
    is_active: bool = True