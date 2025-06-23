# Import necessary components from the agents framework and standard Python libraries
from agents import Agent, Runner, function_tool, WebSearchTool
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from logger import logger



# Define the main class responsible for managing the AI agents
class CareerAgent():
    def __init__(self):
        logger.info("Initializing CareerAgent")
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
        self.memory = ConversationBufferMemory(return_messages=True)
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=True  # Set to False if you don't want logs
        )
        self.message_history = []
        # Instantiate the main career agent with a specific model and behavior
        self.career_agent = Agent(
            name="CareerAgent",  # Name of the agent
            instructions="""
                You are a helpful and proactive AI career coach.

                When the user tells you about their interests, respond with career suggestions immediately — no need to ask twice.

                Offer specific, relevant career paths and optionally ask a follow-up to refine suggestions. Avoid repeating permission-seeking questions.
                """,
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
                model=os.getenv("MODEL_NAME"),  
                tools=[guardrail_func], 
                handoffs=[self.career_agent]  # Delegate relevant queries to the career agent
        )
    
    # Run the agent workflow with user input
    async def run_agent(self, input: str) -> str:
        logger.info(f"Received input: {input}")
        if not input or not isinstance(input, str):
            return "Please provide a question or some information about your interests."

        prompt = self.build_conversation_prompt(input)

        result = await Runner.run(self.guardrail, prompt)

        if hasattr(result, "handoff_target") and result.handoff_target == self.career_agent:
            logger.info("Handed off to career agent")
            response = await self.conversation.apredict(input=input)
        else:
            response = result.final_output.strip()

        self.message_history.append({"role": "user", "content": input})
        self.message_history.append({"role": "assistant", "content": response})

        logger.info(f"Final result: {response}")
        return response


    def build_conversation_prompt(self, user_input: str) -> str:
        # Convert history into a readable format
        formatted = ""
        for msg in self.message_history:
            formatted += f"{msg['role']}: {msg['content']}\n"
        formatted += f"user: {user_input}"
        return formatted

# Tool function used by the career agent to return a simple career suggestion string
@function_tool
def get_career(career: str) -> str:
    return f"Based on your interests, the career best suited for you is {career}"
    
# Tool function used by the guardrail agent to respond to off-topic inputs
@function_tool
def guardrail_func(query: str) -> str:
    return f"I'm sorry, I am here to help you find your ideal career, not to discuss {query}"


