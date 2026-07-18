"""
J.A.R.V.I.S Model Manager

Controls available AI models.

Profiles:

fast:
    Quick conversations and simple commands

default:
    Main JARVIS assistant

coding:
    Programming and development tasks

vision:
    Future vision model support
"""


class ModelManager:

    def __init__(self):

        self.models = {

            # Fast responses
            "fast": "qwen3:8b",

            # Main assistant
            "default": "jarvis",

            # Coding / development
            "coding": "qwen3:8b",

            # Future image model
            "vision": None,

        }


        self.active = "default"


    def get_active_model(self) -> str:

        return self.models[self.active]


    def set_active(self, profile: str):

        if profile in self.models:

            self.active = profile


    def get_profile(self) -> str:

        return self.active


    def list_models(self):

        return self.models.copy()