"""
Ollama Provider
"""

import json
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

            "stream": True,

            "think": False,

            "options": {

                "temperature": 0.6,

                "num_ctx": 2048,

                "num_predict": 256,

            },
        }


        print("[OLLAMA] Request started")


        response = requests.post(

            f"{self.host}/api/generate",

            json=payload,

            stream=True,

            timeout=120,

        )


        response.raise_for_status()


        answer = []


        for line in response.iter_lines(decode_unicode=True):

            if not line:

                continue


            data = json.loads(line)


            # Normal answer tokens
            if data.get("response"):

                answer.append(
                    data["response"]
                )


            # Safety for models returning thinking text
            if data.get("done"):

                break



        result = "".join(answer).strip()


        print("[OLLAMA] Final length:", len(result))


        return result



    def stream(self, prompt: str):


        payload = {

            "model": self.model,

            "prompt": prompt,

            "stream": True,

            "think": False,

        }


        response = requests.post(

            f"{self.host}/api/generate",

            json=payload,

            stream=True,

            timeout=120,

        )


        response.raise_for_status()



        for line in response.iter_lines(decode_unicode=True):

            if not line:

                continue


            data = json.loads(line)


            token = data.get("response")


            if token:

                yield token



    def get_name(self) -> str:

        return "Ollama"



    def get_model(self) -> str:

        return self.model