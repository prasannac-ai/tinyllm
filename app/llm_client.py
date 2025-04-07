import requests

def query_llm(prompt: str) -> str:
    url = "http://llm:11434/api/generate"
    payload = {
        "model": "tinyllama",
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
