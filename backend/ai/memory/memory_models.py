"""
J.A.R.V.I.S Memory Models

Structured memory objects.
"""


from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any



@dataclass
class MemoryItem:

    key: str

    value: Any

    category: str = "fact"

    created: str = field(
        default_factory=lambda:
        datetime.now().isoformat()
    )



    def to_dict(self):

        return {

            "key": self.key,

            "value": self.value,

            "category": self.category,

            "created": self.created

        }



@dataclass
class ConversationItem:

    role: str

    content: str

    timestamp: str = field(
        default_factory=lambda:
        datetime.now().isoformat()
    )



    def to_dict(self):

        return {

            "role": self.role,

            "content": self.content,

            "timestamp": self.timestamp

        }



@dataclass
class UserProfile:

    data: Dict[str, Any] = field(
        default_factory=dict
    )



    def set(
        self,
        key,
        value
    ):

        self.data[key] = value



    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )