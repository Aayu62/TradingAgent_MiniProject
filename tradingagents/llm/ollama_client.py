import requests

class OllamaClient:
    def __init__(self, model="llama3.1:8b"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        r = requests.post(self.url, json=payload)
        if r.status_code != 200:
            return f"LLM Error: {r.status_code}"
        j = r.json()
        return j.get("response", "")
