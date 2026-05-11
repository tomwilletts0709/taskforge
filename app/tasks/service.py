from app.tasks.repository import TaskRepository
from app.tasks.models import Tasks
from app.domain import TaskStatus, can_transition

class TaskService: 
    def __init__(self, task_repo: TaskRepository): 
        self.task_repo = task_repo


    def create_task(self, title: str, project_id: int):
         
        if not title or title.strip() == "":
            raise ValueError("No Title Found")
        
        if project_id is None:
            raise ValueError("No project ID Found")

        task = Tasks(
            title = title, 
            project_id=project_id
         )

        task = self.task_repo.create_task(task)
            
        return task


    def change_task_status(self, task_id: int, new_status: str):
        task = self.task_repo.get_task(task_id)

        if not can_transition(task.status, new_status): 
            raise ValueError("Invalid Status")
        
        task = self.task_repo.change_task_status(task_id, new_status)

        return task
        

    def update_task_title(self, task_id: int, new_title: str, current_user_id: int): 
        if not new_title or new_title.strip() == "": 
            raise ValueError("New Title Cannot Be Updated")
        
        task = self.task_repo.update_task(task_id, new_title)
        return task    