# Git REST Lab 2

A simple REST service created for a university laboratory project.

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- uv
- Docker
- Dev Container

## Setup

Synchronize the project dependencies:

```bash
uv sync
```

Run the service with Uvicorn:

```bash
uv run uvicorn git_rest_lab2.main:app --reload
```

The service is available at [http://localhost:8000](http://localhost:8000).
Interactive Swagger documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

## Endpoints

- `GET /` returns a message confirming that the service is running.
- `GET /health` returns the service health status.
Commit changes new

## Quality and Security Checks

This project uses GitHub Actions to automate code quality and security checks.

- **Ruff** — Python linting.
- **Pytest** — automated unit tests.
- **Codecov** — test coverage reporting.
- **Allure Report** — published test reports.
- **SonarQube Cloud** — static code analysis.
- **Snyk Open Source** — dependency vulnerability scanning.
- **Snyk Code** — source code security scanning.
- **Dependabot** — dependency monitoring and updates.

Pull requests are checked automatically before merging into `main`.
