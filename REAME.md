# 🧠 AI Career Advisor Agent

An interactive, memory-enabled AI career coach built with OpenAI's GPT API, LangChain, and a React front end. This agent helps users explore career paths based on their interests, strengths, and values through a natural conversation.

## 🚀 Features
✅ Career-focused guidance powered by GPT-4o

✅ Guardrails to keep conversations on-topic

✅ Memory for multi-turn conversations (via LangChain)

✅ React Frontend for real-time chat UI

✅ FastAPI Backend for async LLM handling

✅ Tool-augmented responses using custom career suggestion functions

## 🧱 Tech Stack
Frontend

React (via Vite)

Axios

Backend

FastAPI (Python)

OpenAI API

LangChain

Custom agents with agents framework



## 🧪 Getting Started
### 🔧 Backend Setup
Clone the repo

bash
Copy
Edit
git clone https://github.com/your-username/ai-career-agent
cd ai-career-agent
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create .env file

env
Copy
Edit
OPENAI_API_KEY=your-key-here
MODEL_NAME=gpt-4o
Run FastAPI server

bash
Copy
Edit
uvicorn main:app --reload
Backend runs at: http://localhost:8000

## 💻 Frontend Setup
Open a new terminal and navigate to the frontend folder.

bash
Copy
Edit
cd frontend
npm install
Run the React app

bash
Copy
Edit
npm run dev
Frontend runs at: http://localhost:5173

## 📡 API Endpoint
Method	Endpoint	Description
POST	/ask	Send user input to the AI agent
POST	/reset	 Reset conversation (Coming Soon)

Example request:

json
Copy
Edit
POST /ask
{
  "input": "I enjoy working with animals and being outdoors."
}
## 🤖 Agent Logic Overview
GuardrailAgent filters off-topic questions.

CareerAgent gives career advice based on user interests.

LangChain Memory stores multi-turn context.

Custom tools like get_career() allow the agent to return structured results.

## 📈 Example Use Cases
Students exploring majors or fields

Career changers seeking direction

Job seekers looking for role-fit guidance

## 🛠 Future Improvements
 Store chat history in a database

 Add voice input/output

 Support multi-language interactions

 Admin dashboard for analytics

