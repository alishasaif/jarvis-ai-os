"""
J.A.R.V.I.S AI Provider Manager

Controls which AI provider is used.
Currently:
- Ollama

Future:
- OpenAI
- Gemini
- llama.cpp
- Other local models
"""


from backend.ai.providers.ollama_provider import OllamaProvider


class AIManager:


    def __init__(self):

        self.provider = OllamaProvider()


    def generate(self, prompt: str) -> str:

        return self.provider.generate(prompt)


    def get_provider_name(self):

        return self.provider.get_name()


    def get_model_name(self):

        return self.provider.get_model()