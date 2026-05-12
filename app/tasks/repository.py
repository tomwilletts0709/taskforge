from sqlalchemy import select
from sqlalchemy.orm import Session

from app.tasks.models import Tasks

class TaskRepository:
    def __init__(self, db: Session): 
        self.db = db

    def create_task(self, task: Tasks):
        self.db.add(task)   
        self.db.commit()
        self.db.refresh(task)
        return task
    
    def update_task(self, task_id: int, title: str): 
        statement = select(Tasks).where(Tasks.id == task_id)
        task = self.db.execute(statement).scalars().first()

        if task is None: 
            raise ValueError("No ID Found")
        
        task.title = title
        
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task_status(self, task_id: int, new_status: str): 
        statement = select(Tasks).where(Tasks.id == task_id)
        task = self.db.execute(statement).scalars().first()

        if task is None: 
            raise ValueError("No Task Found")
        
        task.status = new_status
        
        self.db.commit()
        self.db.refresh(task)
        return task

    
    def get_task(self, task_id: int):
        statement = select(Tasks).where(Tasks.id == task_id)
        result = self.db.execute(statement).scalars().first()
        if result is None: 
            raise ValueError("No ID Found")
        return result
    
    def list_tasks(self) -> list[Tasks]: 
        statement = select(Tasks)
        tasks = self.db.execute(statement).scalars().all()
        return tasks

    
    def delete_task(self, task_id: int): 
        statement = select(Tasks).where(Tasks.id == task_id)
        task = self.db.execute(statement).scalars().first()
        if task is None: 
            raise ValueError("No ID Found")
        
        self.db.delete(task)
        self.db.commit()

    

        
