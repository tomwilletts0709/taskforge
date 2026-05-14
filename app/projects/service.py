from app.projects.repository import ProjectRepository
from app.projects.models import Projects


class ProjectService: 

    def __init__(self, project_repo=ProjectRepository):
        self.project_repo = project_repo


    def create_project(self, project_id: int, title: str, description: str):

        if not title or title.strip() == "":
            raise ValueError("Title Not Found")
        
        if project_id is None: 
            raise ValueError("Project Not Found")
        
        project = Projects(
            project_id=project_id,
            title=title.strip(),
            description=description
        )

        project = self.project_repo.create_project(project)
        return project
    
    def update_project(self, project_id:int, title: str, description: str):
        if project_id is None:
            raise ValueError("Project Not Found")

        if not title or title.strip() == "":
            raise ValueError("Title Not Found")

        project = self.project_repo.update_project(
            project_id=project_id,
            title=title.strip(),
            description=description,
        )
        return project
    
    def get_project(self, project_id: int):

        project = self.project_repo.get_project(project_id)
        return project
        
    def list_projects(self) -> list[Projects]:
        projects = self.project_repo.list_projects()
        return projects

    def delete_project(self, project_id: int): 

        project = self.project_repo.get_project(project_id)
        
        if project is None: 
            raise ValueError("Project Not Found")
        
        self.project_repo.delete_project(project_id)

        return None
    

    
