"""
J.A.R.V.I.S Memory Engine

Central access point for all memory operations.

Author: J.A.R.V.I.S AI OS
"""

from backend.ai.memory.memory_manager import MemoryManager


class MemoryEngine:

    def __init__(self):

        self.manager = MemoryManager()

    # -------------------------------------------------
    # Basic Memory
    # -------------------------------------------------

    def remember(self, key: str, value):

        self.manager.remember(
            key,
            value
        )

    def recall(self, key=None):

        return self.manager.recall(
            key
        )

    # -------------------------------------------------
    # Preferences
    # -------------------------------------------------

    def set_preference(self, key, value):

        data = self.manager.recall()

        prefs = data.setdefault(
            "preferences",
            {}
        )

        prefs[key] = value

        self.manager.save()

    def get_preference(self, key):

        data = self.manager.recall()

        return data.get(
            "preferences",
            {}
        ).get(key)

    # -------------------------------------------------
    # Profile
    # -------------------------------------------------

    def set_profile(self, key, value):

        data = self.manager.recall()

        profile = data.setdefault(
            "profile",
            {}
        )

        profile[key] = value

        self.manager.save()

    def get_profile(self):

        return self.manager.recall().get(
            "profile",
            {}
        )

    def profile(self):
        """
        Returns the user profile as readable text.
        Used by AIManager when building prompts.
        """

        profile = self.get_profile()

        if not profile:

            return "No known user information."

        lines = []

        for key, value in profile.items():

            lines.append(
                f"{key}: {value}"
            )

        return "\n".join(lines)

    # -------------------------------------------------
    # Conversation
    # -------------------------------------------------

    def add_message(self, role, text):

        data = self.manager.recall()

        history = data.setdefault(
            "conversation",
            []
        )

        history.append({

            "role": role,

            "content": text

        })

        if len(history) > 30:

            history[:] = history[-30:]

        self.manager.save()

    def history(self, limit=20):

        data = self.manager.recall()

        return data.get(
            "conversation",
            []
        )[-limit:]

    # -------------------------------------------------

    def clear_history(self):

        data = self.manager.recall()

        data["conversation"] = []

        self.manager.save()


memory_engine = MemoryEngine()