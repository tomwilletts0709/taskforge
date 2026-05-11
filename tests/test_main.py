import pytest
from app.main import app
from fastapi.testclient import TestClient
import json

client = TestClient(app)


def test_main(): 
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Server": "Is Running!"}
