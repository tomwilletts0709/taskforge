import pytest
from app.domain import TaskStatus

def test_create_task(task_service):
    task = task_service.create_task(title="Task 1", project_id=1)

    assert task.title == "Task 1"
    assert task.project_id == 1
    

def test_get_task(task_service): 
    created_task = task_service.create_task(
        title="Task 1",
        project_id=1
    )

    task = task_service.get_task(created_task.id)

    assert task.id == created_task.id

def test_update_task_status(task_service):
    created_task = task_service.create_task(
        title="Task 1",
        project_id = 1 
    )

    updated_task = task_service.update_task_status(
        task_id=created_task.id,
        new_status=TaskStatus.IN_PROGRESS,
    )

    assert updated_task.id == created_task.id 
    assert updated_task.status == TaskStatus.IN_PROGRESS.value

def test_delete_task(task_service):
    created_task = task_service.create_task(
        title="Task 1",
        project_id=1
    )

    result = task_service.delete_task(created_task.id)

    assert result is None

    with pytest.raises(ValueError): 
        task_service.get_task(created_task.id)

def test_list_tasks(task_service):
    created_task_1 = task_service.create_task(
        title = "Task 1",
        project_id = 1
    )

    created_task_2 = task_service.create_task(
        title = "Task 2",
        project_id = 1
    )

    tasks = task_service.list_tasks() 

    assert len(tasks) == 2 
    assert created_task_1 in tasks
    assert created_task_2 in tasks 
   

