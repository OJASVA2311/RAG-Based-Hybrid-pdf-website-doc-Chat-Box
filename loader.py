from typing import List
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, DirectoryLoader
from langchain.schema import Document


def load_documents(pdf_path=None, docs_path=None) -> List[Document]:
    documents = []

    if pdf_path:
        print("📄 Loading PDF...")
        loader = PyMuPDFLoader(pdf_path)
        documents.extend(loader.load())

    if docs_path:
        print("📂 Loading TXT documents...")
        loader = DirectoryLoader(
            docs_path,
            glob="**/*.txt",
            loader_cls=TextLoader
        )
        documents.extend(loader.load())

    return documents
