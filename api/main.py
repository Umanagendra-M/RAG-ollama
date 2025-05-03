
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

import os
import shutil

app = FastAPI()

CHROMA_DIR = "/app/chroma"
DATA_DIR = "/app/data"
os.makedirs(DATA_DIR, exist_ok=True)

# Use Docker service name for base_url
OLLAMA_BASE_URL = "http://ollama:11434"

# Reload existing Chroma DB or create new one
embeddings = OllamaEmbeddings(model="llama3.2:3b", base_url=OLLAMA_BASE_URL)
if os.path.exists(os.path.join(CHROMA_DIR, "chroma.sqlite3")):
    vectorstore = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
else:
    loader = TextLoader(f"{DATA_DIR}/sample.txt")
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)
    vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=CHROMA_DIR)
    vectorstore.persist()

retriever = vectorstore.as_retriever()
llm = Ollama(model="llama3.2:3b", base_url=OLLAMA_BASE_URL)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

class Query(BaseModel):
    question: str

@app.post("/query")
def query_rag(q: Query):
    answer = qa_chain.run(q.question)
    return {"answer": answer}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filepath = os.path.join(DATA_DIR, file.filename)
    with open(filepath, "wb") as f:
        shutil.copyfileobj(file.file, f)

    loader = TextLoader(filepath)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)
    vectorstore.add_documents(docs)
    vectorstore.persist()
    return {"status": "uploaded and indexed", "filename": file.filename}
