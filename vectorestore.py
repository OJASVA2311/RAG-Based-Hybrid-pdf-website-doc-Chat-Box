from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma


def create_vector_store(chunks, persist_dir="chroma_db"):
    print("📦 Creating embeddings & vector DB...")

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )

    vectordb.persist()
    print("✅ Vector DB stored")
    return vectordb
