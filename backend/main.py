from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from career_agent import CareerAgent
from logger import logger
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for localhost:3000 (React dev server)
origins = [
    "http://localhost:3000",
    # Add other origins if you deploy frontend elsewhere
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Or use ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

career_agent = CareerAgent()

class QueryRequest(BaseModel):
    input: str

@app.post("/api/chat")
async def ask_agent(query: QueryRequest):
    print("Agent has been asked")
    logger.info(f"API received input: {query.input}")
    result = await career_agent.run_agent(query.input)
    logger.info("API returning result")
    return {"response": result}
