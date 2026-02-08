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


📂 Project Structure
Hybrid-RAG-System/
│
├── main.py # Entry point
├── loader.py # Document loading
├── splitter.py # Chunking logic
├── vectorstore.py # Embeddings & vector DB
├── retrievers.py # MMR, BM25, RRF logic
├── llm.py # LLM configuration
├── chat.py # Chat loop
├── docs/ # Input text documents
└── README.md


