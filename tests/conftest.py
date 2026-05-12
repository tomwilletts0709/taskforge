import pytest
from app.tasks.service import TaskService

@pytest.fixture
def fake_repo(): 
    return FakeTaskRepo()

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


    