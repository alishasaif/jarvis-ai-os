from backend.ai.manager import AIManager
from backend.ai.memory.memory_engine import memory_engine
from backend.ai.router.intent_router import IntentRouter

from difflib import SequenceMatcher


class JarvisCore:

    def __init__(self):

        self.ai = AIManager()
        self.router = IntentRouter()


    # ======================================
    # FUZZY MATCH HELPER
    # ======================================

    def similar(self, text, patterns, threshold=0.65):

        text = text.lower()

        for pattern in patterns:

            score = SequenceMatcher(
                None,
                text,
                pattern
            ).ratio()

            if score >= threshold:
                return True

        return False



    def ask(self, prompt: str) -> str:

        prompt = str(prompt).strip()


        if not prompt:

            return "I did not receive a command, Sir."



        lower = prompt.lower()



        # ======================================
        # DIRECT COMMAND ROUTER
        # ======================================

        route = self.router.route(prompt)


        if route["type"] == "direct":

            response = route["response"]


            memory_engine.add_message(
                "user",
                prompt
            )

            memory_engine.add_message(
                "assistant",
                response
            )


            return response



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



                if key.startswith("my "):

                    key = key[3:]



                if self.similar(
                    key,
                    [
                        "favourite language",
                        "favorite language",
                        "fav language",
                        "favorete language"
                    ]
                ):


                    memory_engine.set_preference(
                        "favourite_language",
                        value.capitalize()
                    )


                    response = (
                        f"I'll remember that your favourite language is {value.capitalize()}, Sir."
                    )


                    memory_engine.add_message(
                        "user",
                        prompt
                    )


                    memory_engine.add_message(
                        "assistant",
                        response
                    )


                    return response



                memory_engine.remember(
                    key,
                    value
                )


                response = (
                    f"I'll remember that your {key} is {value}, Sir."
                )


                memory_engine.add_message(
                    "user",
                    prompt
                )

                memory_engine.add_message(
                    "assistant",
                    response
                )


                return response



            return (
                "Please tell me what you would like me to remember, Sir."
            )



        # ======================================
        # MEMORY RECALL
        # ======================================


        if self.similar(
            lower,
            [
                "what is my favourite language",
                "what is my favorite language",
                "whats my favourite language",
                "whats my favorite language",
                "what is my fav language",
                "what is my favorete language",
                "which language do i like"
            ]
        ):


            value = memory_engine.get_preference(
                "favourite_language"
            )



            if value:


                response = (
                    f"Sir, your favourite language is {value}."
                )


            else:


                response = (
                    "I don't have your favourite language stored yet, Sir."
                )



            memory_engine.add_message(
                "user",
                prompt
            )


            memory_engine.add_message(
                "assistant",
                response
            )


            return response



        # ======================================
        # CONVERSATION MEMORY
        # ======================================


        if (
            "what were we talking about" in lower
            or
            "what did we talk about" in lower
        ):


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

                response = (
                    "Sir, our recent topics were: "
                    +
                    ", ".join(topics[-3:])
                )

            else:

                response = (
                    "We have not discussed anything yet, Sir."
                )



            memory_engine.add_message(
                "user",
                prompt
            )


            memory_engine.add_message(
                "assistant",
                response
            )


            return response



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