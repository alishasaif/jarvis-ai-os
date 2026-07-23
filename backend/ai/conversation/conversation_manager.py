"""
J.A.R.V.I.S Conversation Manager

Maintains recent conversation history.
"""

from backend.ai.memory.memory_engine import memory_engine


class ConversationManager:

    def __init__(self):

        self.memory = memory_engine

    # ---------------------------------------------

    def add_user(self, text: str):

        self.memory.add_message(
            "user",
            text
        )

    # ---------------------------------------------

    def add_assistant(self, text: str):

        self.memory.add_message(
            "assistant",
            text
        )

    # ---------------------------------------------

    def history(self, limit=10):

        return self.memory.history(limit)

    # ---------------------------------------------

    def clear(self):

        self.memory.clear_history()

    # ---------------------------------------------

    def build_prompt(
        self,
        prompt: str,
        limit=10
    ) -> str:

        history = self.history(limit)

        lines = []

        for item in history:

            role = item["role"].capitalize()

            content = item["content"]

            lines.append(
                f"{role}: {content}"
            )

        lines.append(
            f"User: {prompt}"
        )

        lines.append(
            "Assistant:"
        )

        return "\n".join(lines)


conversation_manager = ConversationManager()