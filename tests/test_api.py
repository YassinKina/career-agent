from fastapi.testclient import TestClient

import os, sys
sys.path.append(os.getenv("PYTHONPATH"))
from backend.main import app  # Import the FastAPI app instance from your main module
from backend.utils import log_current_function


# Test the /ask endpoint with a valid input payload
def test_ask_endpoint(client):
    log_current_function()
    payload = {
        "input": "What career suits someone who likes math?"
    }
    response = client.post("/ask", json=payload)
    assert response.status_code == 200  # Expect HTTP 200 OK
    data = response.json()
    assert "response" in data           # Ensure 'response' key is present
    assert isinstance(data["response"], str)  # Response should be a string
    assert len(data["response"]) > 0    # Response should not be empty

# Test the /ask endpoint with an empty string as input
def test_ask_endpoint_empty_input(client): #client is passed in through conftest file
    log_current_function()
    payload = {"input": ""}
    response = client.post("/ask", json=payload)
    assert response.status_code == 200  # Still expect a 200 OK
    json_data = response.json()
    assert "response" in json_data      # Should still receive a response key

# Test the /ask endpoint with missing 'input' key in payload
def test_ask_endpoint_missing_input_key(client):
    log_current_function()
    response = client.post("/ask", json={})
    assert response.status_code == 422  # Expect validation error (Unprocessable Entity)
