from retrievers import hybrid_retriever
from llm import llm


def chat_loop(mmr_retriever, bm25_retriever):
    chat_history = []

    print("\n🤖 RAG Chat Started (type 'exit' to quit)\n")

    while True:
        query = input("🧑 You: ")

        if query.lower() == "exit":
            print("👋 Bye!")
            break

        docs = hybrid_retrieve(query, mmr_retriever, bm25_retriever)

        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
You are a helpful assistant.
Use the context below to answer.

Context:
{context}

Chat History:
{chat_history}

Question:
{query}
"""

        response = llm.invoke(prompt)
        answer = response.content

        print(f"\n🤖 AI: {answer}\n")

        chat_history.append(("User", query))
        chat_history.append(("AI", answer))
