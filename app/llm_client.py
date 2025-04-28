import requests
from retriever import Retriever
from build_knowledge_base import build_knowledge_base


def query_llm(prompt: str) -> str:
    url = "http://llm:11434/api/generate"
    payload = {
        "model": "gemma:2b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            return "LLM failed to respond."
    except Exception as e:
        return f"Error querying LLM: {e}"

def query_with_text_rag(question: str, directory_path: str = "./texts") -> str:
    print("Context:", "in query_with_text_rag")
    texts = build_knowledge_base(directory_path)
    retriever = Retriever(texts)
    context = "\n".join(retriever.get_relevant_docs(question, k=3))
    # prompt = f"""Use the following context to answer the question.
    prompt = f""" Strictly, Only use the following context to answer the question. If the answer is not in the context, say "I don't know."

    Context:    
    {context}

    Question:
    {question}
    """
    return query_llm(prompt=prompt)


