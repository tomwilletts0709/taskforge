# TaskForge API

TaskForge is a small FastAPI project management API built as Project 2 in a
20-project FastAPI learning path.

The aim of this project is to move beyond basic CRUD by modelling users,
projects, tasks, task status transitions, dependency injection, repository
boundaries, and audit log foundations.

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic v2
- SQLite
- Pytest
- Ruff
- uv

## Project Structure

```text
app/
  audit/       Audit log models, repository, and service
  projects/    Project schemas, router, service, repository, and model
  tasks/       Task schemas, router, service, repository, and model
  users/       User schemas, router, service, repository, and model
  db.py        SQLAlchemy engine, session, and database initialization
  deps.py      FastAPI dependencies
  domain.py    Shared enums and domain rules
  main.py      FastAPI app entry point

docs/          Planning and implementation notes
tests/         Unit and router tests
```

The app uses a layered structure:

- Routers handle HTTP requests and responses.
- Services enforce business rules.
- Repositories handle persistence.
- Dependencies wire database sessions into the application.

## Features

- Create, list, get, update, and delete projects.
- Create, list, get, update, and delete tasks.
- Create, list, get, and delete users.
- Validate user password confirmation.
- Validate task title and project fields with Pydantic.
- Enforce task status transitions through shared domain rules.
- Use SQLite for local persistence.

## API Routes

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Health check |
| `POST` | `/projects` | Create a project |
| `GET` | `/projects` | List projects |
| `GET` | `/projects/{project_id}` | Get a project |
| `PATCH` | `/projects/{project_id}` | Update a project |
| `DELETE` | `/projects/{project_id}` | Delete a project |
| `POST` | `/tasks` | Create a task |
| `GET` | `/tasks` | List tasks |
| `GET` | `/tasks/{task_id}` | Get a task |
| `PATCH` | `/tasks/{task_id}` | Update a task title or status |
| `DELETE` | `/tasks/{task_id}` | Delete a task |
| `POST` | `/users` | Create a user |
| `GET` | `/users` | List users |
| `GET` | `/users/{user_id}` | Get a user |
| `DELETE` | `/users/{user_id}` | Delete a user |

## Getting Started

Install dependencies:

```bash
uv sync
```

Run the API:

```bash
uv run uvicorn app.main:app --reload
```

The app runs at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive docs are available at:

```text
http://127.0.0.1:8000/docs
```

## Database

The default database is SQLite:

```text
taskforge.db
```

Tables are created from the SQLAlchemy models through `init_db()` in
`app/db.py`.

## Running Tests

Run the test suite:

```bash
uv run pytest
```

Run Ruff:

```bash
uv run ruff check .
```

## Notes

This project is intentionally small and educational. The current focus is on
clean application boundaries and service-level business rules before adding
larger production concerns such as authentication, authorization, migrations,
and deployment.
