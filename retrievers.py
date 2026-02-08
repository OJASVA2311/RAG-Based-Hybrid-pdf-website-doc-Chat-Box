from typing import List
from langchain.schema import Document
from langchain.retrievers import BM25Retriever


def get_mmr_retriever(vectordb):
    return vectordb.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.5
        }
    )


def get_bm25_retriever(chunks):
    bm25 = BM25Retriever.from_documents(chunks)
    bm25.k = 4
    return bm25


def reciprocal_rank_fusion(results: List[List[Document]], k=60):
    scores = {}

    for docs in results:
        for rank, doc in enumerate(docs):
            doc_id = doc.page_content
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (rank + k)

    ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked_docs


def hybrid_retrieve(query, mmr_retriever, bm25_retriever):
    mmr_docs = mmr_retriever.get_relevant_documents(query)
    bm25_docs = bm25_retriever.get_relevant_documents(query)

    fused = reciprocal_rank_fusion([mmr_docs, bm25_docs])
    final_docs = [Document(page_content=d[0]) for d in fused[:4]]
    return final_docs
