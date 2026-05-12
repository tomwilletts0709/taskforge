from app.tasks.service import TaskService
from app.domain import TaskStatus

import pytest

def test_create_task(TaskService):
    data = create_task(title="Task 1", project_id=1)

    task = TaskService.create_task(data)

    assert create_task.title == "Task 1"
    assert create_task.project_id == 1



    
    
def test_create_task(TaskService):

def test_get_task(TaskService): 

def update_task_status(TaskService):

def test_delete_task(TaskService):

def test_list_tasks(TaskService): 
