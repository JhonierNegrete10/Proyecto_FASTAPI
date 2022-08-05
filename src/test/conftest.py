
import pytest
from starlette.testclient import TestClient
import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\'))
from app.core.config import settings
from app.main import app

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here