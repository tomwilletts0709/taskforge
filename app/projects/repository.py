from sqlalchemy import select
from sqlalchemy.orm import Session

from app.projects.models import Projects

class ProjectRepository:
    def __init__(self, db:Session):
        self.db = db

    def create_project(self, project:Projects)-> Projects: 
        self.db.add(project)
        self.db.commit()
        self.db.refresh()
        return
    
    def update_project(self, project_id: int, title: str, description: str):
        statement=select(Projects).where(Projects.id == project_id)
        project = self.db.execute(statement).scalars().first()

        if project is None: 
            raise ValueError("No Project Found")
        
        project.title = title
        project.description = description

        self.db.commit()
        self.db.refresh(project)
        return project
    
    def get_project(self, project_id: int, title: str):
        statement=select.project(Projects).where(Projects.id == project_id)
        result = self.db.execute(statement).scalars().first()

        if result is None:
            raise ValueError("No Project Found")
        return

    def delete_project(self, project_id: int):
        statment=select.project(Projects).where(Projects.id == project_id)
        result = self.db.execute(statement).scalars().first()

        if result is None: 
            raise ValueError("No Project Found")
        
        self.db.delete()
        self.db.refresh(result)
        return

    def list_projects(self):
        statement=select.project(Projects)
        result = self.db.execute(statement).scalars().all()
        return result
    



    
