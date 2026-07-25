from difflib import SequenceMatcher


class IntentRouter:

    def __init__(self):

        self.greetings = {
            "hello": "Hello, Sir.",
            "hi": "Hello, Sir.",
            "hey": "Hello, Sir.",
            "good morning": "Good morning, Sir.",
            "good evening": "Good evening, Sir.",
            "good night": "Good night, Sir."
        }


        self.memory_keywords = [
            "favourite language",
            "favorite language",
            "fav language",
            "fav lang",
            "my language",
            "remember",
            "what do you remember",
            "what were we talking about"
        ]


        self.system_commands = [
            "cpu",
            "ram",
            "disk",
            "battery"
        ]



    def similarity(self, a, b):

        return SequenceMatcher(
            None,
            a,
            b
        ).ratio()



    def fuzzy_match(self, text, choices, threshold=0.75):

        for item in choices:

            score = self.similarity(
                text,
                item
            )

            if score >= threshold:
                return True

        return False



    def route(self, message: str):

        text = str(message).lower().strip()



        # -----------------------------
        # Greetings
        # -----------------------------

        if text in self.greetings:

            return {
                "type": "direct",
                "response": self.greetings[text]
            }



        if self.fuzzy_match(
            text,
            self.greetings.keys()
        ):

            return {
                "type": "direct",
                "response": "Hello, Sir."
            }



        # -----------------------------
        # Memory commands
        # -----------------------------

        if (
            text.startswith("remember")
            or
            any(
                keyword in text
                for keyword in self.memory_keywords
            )
        ):

            return {
                "type": "memory",
                "response": None
            }



        # -----------------------------
        # Typo tolerant memory questions
        # -----------------------------

        words = text.split()

        for word in words:

            if self.similarity(
                word,
                "favourite"
            ) >= 0.70:

                if (
                    "language" in text
                    or
                    "lang" in text
                ):

                    return {
                        "type": "memory",
                        "response": None
                    }



        # -----------------------------
        # System commands
        # -----------------------------

        if text in self.system_commands:

            return {
                "type": "system",
                "response": None
            }



        # -----------------------------
        # AI fallback
        # -----------------------------

        return {
            "type": "ai",
            "response": None
        }