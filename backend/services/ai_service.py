"""
JARVIS AI Service
Connects UI with local Ollama brain
"""

from backend.ai.providers.ollama_provider import OllamaProvider


class AIService:

    def __init__(self):
        self.provider = OllamaProvider(
            model="jarvis"
        )

    def ask(self, message: str) -> str:

        try:
            return self.provider.generate(message)

        except Exception as e:
            return f"AI Error: {str(e)}"