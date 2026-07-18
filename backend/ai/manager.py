"""
J.A.R.V.I.S AI Provider Manager

Controls AI providers and selected models.

Current:
- Ollama

Future:
- OpenAI
- Gemini
- llama.cpp
- Other local providers
"""


from backend.ai.providers.ollama_provider import OllamaProvider
from backend.ai.model_manager import ModelManager



class AIManager:


    def __init__(self):

        self.model_manager = ModelManager()

        self.provider = OllamaProvider(
            model=self.model_manager.get_active_model()
        )



    def generate(self, prompt: str) -> str:

        return self.provider.generate(prompt)



    def switch_model(self, profile: str):

        self.model_manager.set_active(profile)

        self.provider.model = (
            self.model_manager.get_active_model()
        )



    def get_provider_name(self):

        return self.provider.get_name()



    def get_model_name(self):

        return self.provider.get_model()



    def get_active_profile(self):

        return self.model_manager.get_profile()