# Groq Chatbot

A fast, free CLI chatbot powered by Groq and Llama 3.3 70B. The bot features persistent conversation memory and is fully containerized with Docker for easy setup and deployment.

## Features

- Fast responses using Groq inference
- Persistent memory (conversation history is saved automatically)
- Fully Dockerized application
- Easy configuration through environment variables
- Clean and simple codebase using OpenAI-compatible SDK

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```
### 2. Set up your Groq API Key
Create a .env file in the root directory:
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
echo "MODEL=llama-3.3-70b-versatile" >> .env
You can get your free API key from: https://console.groq.com/keys
### 3. Run the chatbot
Using Docker Compose (recommended):
```bash
docker-compose up --build
```
Or run interactively:
```bash
docker-compose run --rm chatbot
```
## How to Use
Once the bot starts, you will see the message:
Groq Chatbot is ready! (Type 'exit', 'quit', or 'bye' to stop)
Type your message and press Enter to chat
Type exit, quit, or bye to stop the bot
Your conversation history is automatically saved in app/data/conversations.json
## Project Structure
```bash
LLM_Chatbot/
├── app/
│   ├── main.py
│   ├── chatbot.py
│   ├── config.py
│   ├── memory.py
│   └── data/
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
## Technologies
Python 3.11
Groq API (Llama 3.3 70B)
OpenAI Python SDK
Docker & Docker Compose