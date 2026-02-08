Hybrid RAG System (PDF + Document Chatbot)

Hybrid Retrieval-Augmented Generation (RAG):- system that allows users to chat with PDFs and text documents using **MMR + BM25 + Reciprocal Rank Fusion**, powered by a **local LLM (Ollama)**.


🚀 Features

- 📄 Load and process PDFs & TXT documents
- ✂️ Smart document chunking
- 🔍 Hybrid retrieval:
  - MMR (semantic search)
  - BM25 (keyword-based search)
  - Reciprocal Rank Fusion (RRF)
- 🤖 Local LLM using Ollama (privacy-friendly)
- 💬 Chat interface with conversation history
- 📦 Persistent vector storage using ChromaDB

---
 🛠️ Tech Stack 
 
*Python
*LangChain
*ChromaDB
*Ollama
*BM25 Retriever
*MMR Retriever

## ▶️ Run the Project Locally

This project is designed to be run **locally** on your machine.

### 🔧 Prerequisites

Make sure you have the following installed:

- **Python 3.9+**
- **Git**
- **Ollama** (for running the local LLM)

---
HOW TO RUN THIS CODE
1 pip install -r requirements.txt
2 ollama serve
3 ollama pull llama3.1:8b
  ollama pull nomic-embed-text
4 Place your .txt files inside the docs/ folder
(Optional) Add a PDF file and update the path in main.py
5️⃣ Run the Application
python main.py
6️⃣ Ask Questions

Once the program starts, type your question in the terminal:

You: What is this document about?


7 Type exit to quit the application.


