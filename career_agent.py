# Import necessary components from the agents framework and standard Python libraries
from agents import Agent, Runner, function_tool, WebSearchTool
import sys
import os
from logger import logger
from fastapi import FastAPI, Request
from pydantic import BaseModel
import asyncio

# Define the main class responsible for managing the AI agents
class CareerAgent():
    def __init__(self):
        logger.info("Initializing CareerAgent")
        # Instantiate the main career agent with a specific model and behavior
        self.career_agent = Agent(
              name="CareerAgent",  # Name of the agent
              instructions="You are an expert at helping people figure out what career is the best fit for them based on what they tell you about their interests",
              model= os.getenv("MODEL_NAME"),  # Use model name from environment variables
              tools=[get_career]  # Register the get_career tool function
        )

        # Define a guardrail agent to filter or redirect off-topic queries
        self.guardrail = Agent(
                name="GuardrailAgent",  # Name of the agent
                instructions=( 
                    "Help the user with their questions."
                    "If they mention topics unrelated to careers, apologize and then remind them you are here to answer career-related questions."
                    "If they ask about careers and/or tell you about their interests, handoff to career agent."
                ),
                model=os.getenv("MODEL_NAME"),  # Use same model for consistency
                tools=[guardrail_func],  # Register the guardrail handling tool
                handoffs=[self.career_agent]  # Delegate relevant queries to the career agent
        )
    
    # Run the agent workflow with user input
    async def run_agent(self, input: str):
        logger.info(f"Received input: {input}")
        # Validate input: ensure it's not None
        if input is None:
            raise ValueError("Input cannot be None")
        
        # Validate input type: must be a string
        if not isinstance(input, str):
            raise TypeError("Input must be a string")
        
        print("Tell CareerBot about your interests and/or ask questions to determine your ideal career. \n")
        
        # Run the guardrail agent with the input; it will route or process accordingly
        result = await Runner.run(self.guardrail, input)

        logger.info(f"Final result: {result.final_output}")
        # Return only the final output from the agent interaction
        return result.final_output

        # Optional: write result to file (currently commented out)
        # with open("output.txt", "w") as f:
        #     f.write(result.final_output)

# Tool function used by the career agent to return a simple career suggestion string
@function_tool
def get_career(career: str) -> str:
    return f"Based on your interests, the career best suited for you is {career}"
    
# Tool function used by the guardrail agent to respond to off-topic inputs
@function_tool
def guardrail_func(query: str) -> str:
    return f"I'm sorry, I am here to help you find your ideal career, not to discuss {query}"

# NOTE: Previously defined guardrail_agent is not used; this line is commented out
# self.guardrail = guardrail_agent
