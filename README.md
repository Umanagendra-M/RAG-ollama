# RAG with Ollama in Docker (Windows 11)

This project sets up a production-ready Retrieval-Augmented Generation (RAG) system using [Ollama](https://ollama.com) for local LLM inference and FastAPI for serving responses. It is containerized using Docker and works on Windows 11.

## 🧱 Features

- Ollama model server (`llama3`) running in Docker
- FastAPI backend to handle RAG queries
- ChromaDB for local vector storage
- Docker Compose for orchestration

## 🚀 Quickstart




git clone https://github.com/your-username/RAG-ollama.git

after you clone the setup

cd RAG-ollama

docker-compose up --build


to test the setup


curl http://localhost:8000/query -X POST -H "Content-Type: application/json" -d '{"question": "What is RAG?"}'


## 🧱 Features

- open http://localhost:8000/docs in your browser to open the setup and querying the API.

limitations:
Please note that only .txt files can be used for RAG purpose, will try to add support to other type of documents in the future versions.
