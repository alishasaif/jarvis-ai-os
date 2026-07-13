"""
Ollama Provider
"""

import requests

from backend.ai.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def __init__(
        self,
        host: str = "http://127.0.0.1:11434",
        model: str = "jarvis",
    ):
        self.host = host
        self.model = model

    def is_available(self) -> bool:
        try:
            response = requests.get(
                f"{self.host}/api/tags",
                timeout=2,
            )

            return response.status_code == 200

        except Exception:
            return False

    def generate(self, prompt: str) -> str:

        payload = {
    "model": self.model,
    "prompt": prompt,
    "stream": False,
    "think": False,
    "options": {
        "temperature": 0.6,
        "num_ctx": 2048,
    },
}

        response = requests.post(
            f"{self.host}/api/generate",
            json=payload,
            timeout=120,
        )

        response.raise_for_status()

        return response.json()["response"]

    def stream(self, prompt: str):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True,
        }

        response = requests.post(
            f"{self.host}/api/generate",
            json=payload,
            stream=True,
        )

        for line in response.iter_lines():

            if line:

                import json

                data = json.loads(line)

                if "response" in data:
                    yield data["response"]

    def get_name(self) -> str:
        return "Ollama"

    def get_model(self) -> str:
        return self.model