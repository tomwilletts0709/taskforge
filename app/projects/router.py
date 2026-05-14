from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.projects.service import ProjectService
from app.projects.schemas import CreateProject, UpdateProject, ReadProject
from app.projects.repository import ProjectRepository
from app.deps import get_db


router = APIRouter()


def get_project_service(db: Session = Depends(get_db)):
    repository = ProjectRepository(db)
    return ProjectService(repository)


@router.post("/projects", response_model=ReadProject, status_code=201)
async def create_project(
    payload: CreateProject,
    service: ProjectService = Depends(get_project_service),
):
    return service.create_project(
        title=payload.title,
        description=payload.description,
    )


@router.get("/projects", response_model=list[ReadProject], status_code=200)
async def list_projects(
    service: ProjectService = Depends(get_project_service),
):
    return service.list_projects()


@router.get("/projects/{project_id}", response_model=ReadProject, status_code=200)
async def get_project(
    project_id: int,
    service: ProjectService = Depends(get_project_service),
):
    try:
        return service.get_project(project_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="No Project Found")


@router.delete("/projects/{project_id}", status_code=204)
async def delete_project(
    project_id: int,
    service: ProjectService = Depends(get_project_service),
):
    try:
        service.delete_project(project_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="No Project Found")


@router.patch("/projects/{project_id}", response_model=ReadProject)
async def update_project(
    project_id: int,
    payload: UpdateProject,
    service: ProjectService = Depends(get_project_service),
):
    try:
        return service.update_project(
            project_id=project_id,
            title=payload.title,
            description=payload.description,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
