"""
J.A.R.V.I.S Memory Utilities

Helper functions for memory processing.
"""


import re
from datetime import datetime



def normalize_key(text: str) -> str:

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9_ ]",
        "",
        text
    )

    text = text.replace(
        " ",
        "_"
    )

    return text.strip()



def normalize_value(value):

    if isinstance(value, str):

        return value.strip()

    return value



def current_time():

    return datetime.now().isoformat()



def contains_any(
    text: str,
    keywords
):

    text = text.lower()

    return any(
        word.lower() in text
        for word in keywords
    )



def clean_sentence(text):

    return (
        text
        .replace(".", "")
        .replace("!", "")
        .replace("?", "")
        .strip()
    )