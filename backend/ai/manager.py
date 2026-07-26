"""
J.A.R.V.I.S AI Manager

Coordinates:
- Personality
- Conversation
- Memory
- AI Provider
"""

from backend.ai.providers.ollama_provider import OllamaProvider
from backend.ai.model_manager import ModelManager

from backend.ai.personality.jarvis_profile import jarvis_profile
from backend.ai.memory.memory_engine import memory_engine
from backend.ai.conversation import conversation_manager


class AIManager:

    def __init__(self):

        self.model_manager = ModelManager()

        self.provider = OllamaProvider(
            model=self.model_manager.get_active_model()
        )

    # ----------------------------------------------------

    def build_prompt(
        self,
        prompt: str
    ) -> str:

        profile = jarvis_profile.system_prompt()

        memories = memory_engine.profile()

        conversation = conversation_manager.build_prompt(
            prompt
        )

        final_prompt = f"""
{profile}

========================
KNOWN USER FACTS
========================

{memories}

========================
RECENT CONVERSATION
========================

{conversation}
"""

        return final_prompt

    # ----------------------------------------------------

    def generate(
        self,
        prompt: str
    ) -> str:

        final_prompt = self.build_prompt(
            prompt
        )

        return self.provider.generate(
            final_prompt
        )

    # ----------------------------------------------------

    def switch_model(
        self,
        profile: str
    ):

        self.model_manager.set_active(profile)

        self.provider.model = (
            self.model_manager.get_active_model()
        )

    # ----------------------------------------------------

    def get_provider_name(self):

        return self.provider.get_name()

    # ----------------------------------------------------

    def get_model_name(self):

        return self.provider.get_model()

    # ----------------------------------------------------

    def get_active_profile(self):

        return self.model_manager.get_profile()