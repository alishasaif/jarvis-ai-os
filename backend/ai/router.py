"""
J.A.R.V.I.S AI Router

Determines whether a user request should be:
1. Executed locally
2. Sent to Ollama
"""

from backend.commands.app_commands import AppCommands
from backend.commands.system_commands import SystemCommands


class AIRouter:

    def __init__(self):
        self.apps = AppCommands()
        self.system = SystemCommands()

    def route(self, prompt: str):

        text = prompt.lower().strip()

        # ----------------------------
        # Open Applications
        # ----------------------------

        if "open chrome" in text:
            return self.apps.open_chrome()

        if "open notepad" in text:
            return self.apps.open_notepad()

        if "open calculator" in text:
            return self.apps.open_calculator()

        # ----------------------------
        # System Information
        # ----------------------------

        if "cpu" in text:
            return self.system.cpu()

        if "ram" in text:
            return self.system.ram()

        if "disk" in text:
            return self.system.disk()

        # ----------------------------
        # Let Ollama Answer
        # ----------------------------

        return None