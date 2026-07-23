"""
J.A.R.V.I.S Memory Manager

Handles loading and saving the memory database.
"""

import json
import os
from datetime import datetime


class MemoryManager:

    def __init__(self):

        self.file = os.path.join(
            os.path.dirname(__file__),
            "memory.json"
        )

        self.data = self.load()

    # -------------------------------------------------

    def default_data(self):

        return {

            "profile": {

                "name": "",
                "nickname": "",
                "occupation": "",
                "location": "",
                "language": "English"

            },

            "preferences": {

                "editor": "",
                "theme": "",
                "shell": "",
                "os": ""

            },

            "projects": {},

            "facts": {},

            "conversation": [],

            "last_updated": ""

        }

    # -------------------------------------------------

    def load(self):

        if not os.path.exists(self.file):

            data = self.default_data()

            self.data = data

            self.save()

            return data

        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

        except Exception:

            data = self.default_data()

        defaults = self.default_data()

        for key, value in defaults.items():

            if key not in data:

                data[key] = value

        return data

    # -------------------------------------------------

    def save(self):

        self.data["last_updated"] = datetime.now().isoformat()

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.data,
                f,
                indent=4,
                ensure_ascii=False
            )

    # -------------------------------------------------

    def remember(self, key, value):

        self.data["facts"][key] = value

        self.save()

    # -------------------------------------------------

    def recall(self, key=None):

        if key is None:

            return self.data

        return self.data["facts"].get(key)