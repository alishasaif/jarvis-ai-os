from PySide6.QtCore import QObject, Signal, Slot

from backend.ai.router import AIRouter
from backend.ai.providers.ollama_provider import OllamaProvider


class AIWorker(QObject):

    finished = Signal(str)
    error = Signal(str)

    listening = Signal()
    thinking = Signal()
    speaking = Signal()

    def __init__(self):

        super().__init__()

        self.router = AIRouter()
        self.ai = OllamaProvider()

    @Slot(str)
    def process(self, text):

        try:

            self.listening.emit()

            result = self.router.route(text)

            if result:

                self.speaking.emit()
                self.finished.emit(result)
                return

            self.thinking.emit()

            answer = self.ai.generate(text)

            self.speaking.emit()

            self.finished.emit(answer)

        except Exception as e:

            self.error.emit(str(e))