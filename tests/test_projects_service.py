import pytest


def test_create_project(project_service): 
    project = project_service.create_project(
        project_id=1,
        title="project 1",
        description="project 1 description",
    )

    assert project.project_id == 1
    assert project.title == "project 1"
    assert project.description == "project 1 description"

def test_get_project(project_service): 
    created_project = project_service.create_project(
        project_id=1,
        title="project 1",
        description="project 1 description",
    )

    project = project_service.get_project(created_project.id)

    assert project.project_id == 1
    assert project.id == created_project.id

def test_delete_project(project_service): 
    created_project = project_service.create_project(
        project_id=1,
        title="project 1",
        description="project 1 description",
    )

    result = project_service.delete_project(created_project.id)

    assert result is None 

    with pytest.raises(ValueError):
        project_service.get_project(created_project.id)

def test_list_project(project_service):
    created_project_1 = project_service.create_project(
        project_id=1,
        title="project 1",
        description="project 1 description",
    )

    created_project_2 = project_service.create_project(
        project_id=2,
        title="project 2",
        description="project 2 description",
    )

    projects = project_service.list_projects()

    assert len(projects) == 2


def test_update_project(project_service):
    created_project = project_service.create_project(
        project_id=1,
        title="project 1",
        description="project 1 description",
    )

    updated_project = project_service.update_project(
        project_id=created_project.id,
        title="project 2",
        description="project 2 description",
    )

    assert updated_project.id == created_project.id
    assert updated_project.title == "project 2"
    assert updated_project.description == "project 2 description"
