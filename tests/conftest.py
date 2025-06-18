# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from backend.main import app
from dotenv import load_dotenv
import os

# Load environment variables before tests run
load_dotenv()

@pytest.fixture(scope="module")
def client():
    """Fixture for creating a test client for FastAPI app."""
    with TestClient(app) as c:
        yield c
