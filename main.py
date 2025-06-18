# Import core components from the agents framework and your own career agent module
from agents import set_default_openai_api, Agent, Runner
from career_agent import CareerAgent
import os
from dotenv import load_dotenv
from logger import logger

# Load environment variables from a .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Set the default OpenAI API key for agent interactions
set_default_openai_api(api_key)

# Import FastAPI and Pydantic for building and validating the API
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Initialize FastAPI app instance
app = FastAPI()

# Create an instance of the CareerAgent class to handle queries
career_agent = CareerAgent()

# Define the expected request body schema using Pydantic
class QueryRequest(BaseModel):
    input: str  # The user's query or career-related input

# Define a POST endpoint that takes in user input and returns the agent's response
@app.post("/ask")
async def ask_agent(query: QueryRequest):
    logger.info(f"API received input: {query.input}")
    # Pass the input to the career agent and await the result
    result = await career_agent.run_agent(query.input)

    logger.info("API returning result")
    
    # Return the result as a JSON response
    return {"response": result}
