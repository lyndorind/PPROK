from fastapi.testclient import TestClient

from git_rest_lab2 import __version__
from git_rest_lab2.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Git REST Lab 2 service is running"
    }


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_hello():
    response = client.get("/hello/Polina")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Polina!"}


def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {
        "service": "Git REST Lab 2",
        "framework": "FastAPI",
    }


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": __version__}
