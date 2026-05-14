import pytest
from app.tasks.service import TaskService
from app.tasks.repository import TaskRepository
from app.projects.repository import ProjectRepository
from app.projects.service import ProjectService


@pytest.fixture
def fake_repo(): 
    return FakeTaskRepo()

@pytest.fixture
def fake_project_repo():
    return FakeProjectRepo()

@pytest.fixture
def project_service(fake_project_repo): 
    return ProjectService(fake_project_repo)

@pytest.fixture
def task_service(fake_repo):
    return TaskService(fake_repo)

class FakeTaskRepo:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task):
        task.id = len(self.tasks) + 1
        self.tasks[task.id] = task
        return task
    
    def update_task(self, task_id: int, title: str): 
        task = self.tasks.get(task_id)

        if task is None: 
            raise ValueError("No ID Found")

        task.title = title
        return task
    
    def update_task_status(self, task_id: int, new_status: str): 
        task = self.tasks.get(task_id)

        if task is None: 
            raise ValueError("No Task Found")
        
        task.status = new_status
        return task

    def get_task(self, task_id: int): 
        task = self.tasks.get(task_id)

        if task is None: 
            raise ValueError("No ID Found")
        
        return task
    
    def list_tasks(self): 
        return list(self.tasks.values())
    
    def delete_task(self, task_id: int): 
        task = self.tasks.get(task_id)

        if task is None: 
            raise ValueError("No ID Found")
        del self.tasks[task.id]
        return task


class FakeProjectRepo:
    def __init__(self):
        self.projects = {}

    def create_project(self, project):
        project.id = len(self.projects) + 1
        self.projects[project.id] = project
        return project

    def get_project(self, project_id: int):
        project = self.projects.get(project_id)

        if project is None:
            raise ValueError("No ID Found")

        return project

    def list_projects(self):
        return list(self.projects.values())

    def update_project(self, project_id: int, title: str, description: str):
        project = self.get_project(project_id)
        project.title = title
        project.description = description
        return project

    def delete_project(self, project_id: int): 
        project = self.projects.get(project_id)

        if project is None: 
            raise ValueError("No ID Found")
        del self.projects[project.id]
        return project
