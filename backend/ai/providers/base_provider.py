"""
Base Provider
Every AI provider must implement this interface.
"""

from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def is_available(self) -> bool:
        """Return True if the provider is ready."""
        pass

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a complete response."""
        pass

    @abstractmethod
    def stream(self, prompt: str):
        """Yield streamed response chunks."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Provider display name."""
        pass

    @abstractmethod
    def get_model(self) -> str:
        """Current model name."""
        pass