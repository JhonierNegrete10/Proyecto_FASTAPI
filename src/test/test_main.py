from starlette.testclient import TestClient
import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))

from app.main import app

client = TestClient(app)


def test_ping(test_app:TestClient):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World!"}