app/
  main.py
  db.py
  dependencies.py

  domain.py

  users/
    models.py
    schemas.py
    repository.py
    service.py
    router.py

  projects/
    models.py
    schemas.py
    repository.py
    service.py
    router.py

  tasks/
    models.py
    schemas.py
    repository.py
    service.py
    router.py
    protocols.py

  audit/
    models.py
    repository.py
    service.py

tests/
  conftest.py
  test_tasks_service.py
  test_tasks_router.py
  test_projects_service.py
  test_permissions.py
  test_audit.py