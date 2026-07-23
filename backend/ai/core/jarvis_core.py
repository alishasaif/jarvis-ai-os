from backend.ai.manager import AIManager
from backend.ai.memory.memory_engine import memory_engine


class JarvisCore:

    def __init__(self):

        self.ai = AIManager()


    def ask(self, prompt: str) -> str:

        prompt = str(prompt).strip()

        if not prompt:
            return "I did not receive a command, Sir."


        lower = prompt.lower()



        # ======================================
        # REMEMBER
        # ======================================

        if lower.startswith("remember"):

            text = prompt[8:].strip()


            if " is " in text.lower():

                key, value = text.lower().split(
                    " is ",
                    1
                )


                key = key.strip()
                value = value.strip()


                # remove "my"
                if key.startswith("my "):
                    key = key[3:]


                # favourite language handling

                if "favourite language" in key or "favorite language" in key:

                    memory_engine.set_preference(
                        "favourite_language",
                        value.capitalize()
                    )

                    return (
                        f"I'll remember that your favourite language is {value.capitalize()}, Sir."
                    )


                memory_engine.remember(
                    key,
                    value
                )


                return (
                    f"I'll remember that your {key} is {value}, Sir."
                )


            return (
                "Please tell me what you would like me to remember, Sir."
            )



        # ======================================
        # RECALL
        # ======================================


        if (
            "favourite language" in lower
            or
            "favorite language" in lower
        ):


            value = memory_engine.get_preference(
                "favourite_language"
            )


            if value:

                return (
                    f"Sir, your favourite language is {value}."
                )


            return (
                "I don't have your favourite language stored yet, Sir."
            )



        # ======================================
        # CONVERSATION MEMORY
        # ======================================


        if "what were we talking about" in lower:


            history = memory_engine.history(
                limit=5
            )


            topics = []


            for item in history:

                if item["role"] == "user":

                    topics.append(
                        item["content"]
                    )


            if topics:

                return (
                    "Sir, our recent topics were: "
                    +
                    ", ".join(topics[-3:])
                )


            return (
                "We have not discussed anything yet, Sir."
            )



        # ======================================
        # NORMAL AI CHAT
        # ======================================


        memory_engine.add_message(
            "user",
            prompt
        )


        response = self.ai.generate(
            prompt
        )


        memory_engine.add_message(
            "assistant",
            response
        )


        return response



    def process(self, prompt):

        return self.ask(prompt)