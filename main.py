from loader import load_documents
from splitter import split_documents
from vectorstore import create_vector_store
from retrievers import get_mmr_retriever, get_bm25_retriever
from chat import chat_loop


if __name__ == "__main__":

    docs = load_documents(
        pdf_path="sample.pdf",
        docs_path="docs"
    )

    chunks = split_documents(docs)

    vectordb = create_vector_store(chunks)

    mmr_retriever = get_mmr_retriever(vectordb)
    bm25_retriever = get_bm25_retriever(chunks)

    chat_loop(mmr_retriever, bm25_retriever)
