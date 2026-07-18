from backend.ai.manager import AIManager


class JarvisCore:
    """
    Main J.A.R.V.I.S Intelligence Core

    Handles:
    - User requests
    - AI processing
    - Future memory
    - Future planning
    - Future tools
    """


    def __init__(self):

        self.ai = AIManager()



    def ask(self, prompt: str) -> str:
        """
        Main entry point used by AIWorker
        """

        prompt = str(prompt).strip()


        if not prompt:

            return "I did not receive a command."


        response = self.ai.generate(
            prompt
        )


        return str(response)



    # Alias for future modules

    def process(self, prompt: str) -> str:

        return self.ask(prompt)