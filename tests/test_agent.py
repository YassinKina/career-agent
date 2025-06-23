import pytest
import os, sys
sys.path.append(os.getenv("PYTHONPATH"))

from backend.career_agent import CareerAgent
from backend.utils import log_current_function

from logger import logger

# Test to ensure basic input produces a valid, relevant response
@pytest.mark.asyncio
async def test_run_agent_basic_response():
    log_current_function()
    
    agent = CareerAgent()
    input_text = "I like problem solving and remote work."
    response = await agent.run_agent(input_text)
    assert isinstance(response, str)  # Response should be a string
    assert len(response) > 0          # Response should not be empty
    assert "career" in response.lower()  # Response should mention 'career' (basic relevance check)

# Test to verify the guardrail catches off-topic input (e.g., unrelated to careers)
@pytest.mark.asyncio
async def test_guardrail_response():
    log_current_function()
    agent = CareerAgent()
    response = await agent.run_agent("Tell me about sports")
    lower_response = response.lower()
    assert (
        "career-related" in lower_response or
        "not to discuss" in lower_response or
        "i'm here to help" in lower_response or
        "please let me know" in lower_response
    ), f"Unexpected guardrail response: {response}"

# Test how the agent handles an empty string input
@pytest.mark.asyncio
async def test_empty_input():
    log_current_function()
    agent = CareerAgent()
    response = await agent.run_agent("")
    assert response is not None
    assert len(response) > 0  # Should still return a response

# Test that passing `None` as input raises a ValueError (input validation)
@pytest.mark.asyncio
async def test_invalid_input():
    log_current_function()
    agent = CareerAgent()
    with pytest.raises(TypeError):
        await agent.run_agent(None)  # Should raise ValueError due to None input

# Test that passing a non-string object raises a TypeError
@pytest.mark.asyncio
async def test_invalid_input_obj():
    log_current_function()
    agent = CareerAgent()

    class Cat():
        def __init__(self, name):
            self.name = name

    cat = Cat("dman and eevee")
    with pytest.raises(TypeError):
        await agent.run_agent(cat)  # Should raise TypeError due to non-string input
