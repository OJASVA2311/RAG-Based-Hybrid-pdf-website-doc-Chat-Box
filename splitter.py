from langchain_text_splitters import CharacterTextSplitter


def split_documents(documents, chunk_size=1000, chunk_overlap=150):
    print("✂️ Chunking documents...")

    splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(documents)
    print(f"✅ Created {len(chunks)} chunks")
    return chunks
