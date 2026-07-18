"""
J.A.R.V.I.S Core

This is the central brain of J.A.R.V.I.S.

Responsibilities:
- Understand user requests
- Execute local commands
- Choose the correct AI model
- Query the AI provider
- Return the final response
"""

from backend.ai.router import AIRouter
from backend.ai.manager import AIManager


class JarvisCore:

    def __init__(self):

        self.router = AIRouter()
        self.ai = AIManager()

    def ask(self, prompt: str) -> str:

        # ---------------------------------
        # Step 1
        # Try executing locally first
        # ---------------------------------

        result = self.router.route(prompt)

        if result is not None:
            return result

        # ---------------------------------
        # Step 2
        # Otherwise ask the AI
        # ---------------------------------

        return self.ai.generate(prompt)