from PySide6.QtCore import QObject, Signal, Slot

from backend.ai.core.jarvis_core import JarvisCore


class AIWorker(QObject):

    finished = Signal(str)
    error = Signal(str)

    listening = Signal()
    thinking = Signal()
    speaking = Signal()

    def __init__(self):

        super().__init__()

        # Central J.A.R.V.I.S Brain
        self.jarvis = JarvisCore()

    @Slot(str)
    def process(self, text):

        print("=" * 60)
        print("[AIWorker] process() started")
        print(f"[AIWorker] Prompt: {text}")
        print("=" * 60)

        try:

            print("[AIWorker] Emitting LISTENING")
            self.listening.emit()

            print("[AIWorker] Emitting THINKING")
            self.thinking.emit()

            print("[AIWorker] Asking Jarvis Core...")
            answer = self.jarvis.ask(text)

            print("[AIWorker] Jarvis Core returned successfully")

            self.speaking.emit()

            print("[AIWorker] Emitting FINISHED")
            self.finished.emit(answer)

            print("[AIWorker] process() completed")

        except Exception as e:

            print("[AIWorker] ERROR")
            print(type(e).__name__)
            print(str(e))

            self.error.emit(str(e))