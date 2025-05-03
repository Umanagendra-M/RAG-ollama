# RAG with Ollama in Docker (Windows 11)

This project sets up a production-ready Retrieval-Augmented Generation (RAG) system using [Ollama](https://ollama.com) for local LLM inference and FastAPI for serving responses. It is containerized using Docker and works on Windows 11.

## 🧱 Features

- Ollama model server (`llama3`) running in Docker
- FastAPI backend to handle RAG queries
- ChromaDB for local vector storage
- Docker Compose for orchestration

## 🚀 Quickstart

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/RAG-ollama.git
cd RAG-ollama
docker-compose up --build

'''
to test the setup

curl http://localhost:8000/query -X POST -H "Content-Type: application/json" -d '{"question": "What is RAG?"}'

