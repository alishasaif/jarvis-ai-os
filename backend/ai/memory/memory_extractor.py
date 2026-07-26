"""
J.A.R.V.I.S Memory Extractor

Extracts user facts and preferences
from natural language.
"""


import re

from backend.ai.memory.memory_utils import (
    normalize_key,
    normalize_value
)



class MemoryExtractor:


    def extract(self, text: str):

        memories = []


        patterns = [

            (
                r"my favourite (.+?) is (.+)",
                "preference"
            ),

            (
                r"my favorite (.+?) is (.+)",
                "preference"
            ),

            (
                r"i use (.+)",
                "fact"
            ),

            (
                r"my name is (.+)",
                "profile"
            ),

            (
                r"i live in (.+)",
                "profile"
            ),

        ]


        clean = text.lower().strip()


        for pattern, category in patterns:

            match = re.search(
                pattern,
                clean
            )


            if match:


                if len(match.groups()) == 2:

                    key = normalize_key(
                        match.group(1)
                    )

                    value = normalize_value(
                        match.group(2)
                    )


                else:

                    key = "fact"

                    value = normalize_value(
                        match.group(1)
                    )


                memories.append({

                    "key": key,

                    "value": value,

                    "category": category

                })


        return memories



memory_extractor = MemoryExtractor()