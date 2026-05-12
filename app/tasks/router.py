from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.tasks.repository import TaskRepository
from app.tasks.schemas import TaskCreate, TaskRead, TaskUpdate
from app.tasks.service import TaskService
from app.deps import get_db


router = APIRouter() 


def get_task_service(db: Session = Depends(get_db)): 
    repository = TaskRepository(db)
    return TaskService(repository)

@router.post("/tasks", response_model=TaskRead, status_code=201)
async def create_task(
    payload: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    return service.create_task(
        title=payload.title,
        project_id=payload.project_id,
    )


@router.get("/tasks", response_model=list[TaskRead])
async def list_tasks(
    service: TaskService = Depends(get_task_service),
):
    return service.list_tasks()


@router.get("/tasks/{task_id}", response_model=TaskRead)
async def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    try:
        return service.get_task(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")


@router.patch("/tasks/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: int,
    payload: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    try:
        if payload.status is not None:
            return service.update_task_status(task_id, payload.status)

        return service.update_task_title(task_id, payload.title)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/tasks/{task_id}", status_code=204)
async def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    try:
        service.delete_task(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")
