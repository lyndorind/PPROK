from fastapi import FastAPI

from git_rest_lab2 import __version__

app = FastAPI(
    title="Git REST Lab 2",
    version=__version__,
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Git REST Lab 2 service is running"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/hello/{name}")
def hello_user(name: str) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}


@app.get("/about")
def about_service() -> dict[str, str]:
    return {
        "service": "Git REST Lab 2",
        "framework": "FastAPI",
    }


@app.get("/version")
def service_version() -> dict[str, str]:
    return {"version": __version__}