from app.tasks.repository import TaskRepository
from app.domain import UserProgress
from app.deps import get_db


class TaskService: 
    def __init__(self, task_repo: TaskRepository, user_progress: UserProgress): 
        self.task_repo = task_repo
        self.user_progress = user_progress

    def create_task(self, title: str, project_id: int): 

        if not title or title.strip() == "":
            raise ValueError("No Title Found")
        
        task = self.task_repo.create_task(create_task)
        
       
    def delete_task(self, title: str, project_id: int) -> TaskService:
        