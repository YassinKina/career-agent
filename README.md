# 🧠 AI Career Advisor Agent (Still in Development)

An interactive, memory-enabled AI career coach built with OpenAI's GPT API, LangChain, and a React front end. This agent helps users explore career paths based on their interests, strengths, and values through a natural conversation.

## 🚀 Features
✅ Career-focused guidance powered by GPT-4o

✅ Guardrails to keep conversations on-topic

✅ Memory for multi-turn conversations (via LangChain)

✅ React Frontend for real-time chat UI

✅ FastAPI Backend for async LLM handling

✅ Tool-augmented responses using custom career suggestion functions

## 🧱 Tech Stack
### Frontend
- React (via Vite)
- Axios

### Backend
- FastAPI (Python)
- OpenAI API
- LangChain
- Custom agents with agents framework

## 🧪 Getting Started
### 🔧 Backend Setup
Clone the repo

```bash
git clone https://github.com/your-username/ai-career-agent
cd ai-career-agent

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```
### 💻 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

| Method | Endpoint | Description                      |
| ------ | -------- | -------------------------------- |
| POST   | /ask     | Send user input to the AI agent  |
| POST   | /reset   | Reset conversation (Coming Soon) |

Example Request
POST /ask
{
  "input": "I enjoy working with animals and being outdoors."
}

