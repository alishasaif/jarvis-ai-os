from PySide6.QtCore import QObject, Signal, Slot

from backend.ai.router import AIRouter
from backend.ai.manager import AIManager


class AIWorker(QObject):

    finished = Signal(str)
    error = Signal(str)

    listening = Signal()
    thinking = Signal()
    speaking = Signal()


    def __init__(self):

        super().__init__()

        self.router = AIRouter()

        # AI Provider Manager
        # Currently uses Ollama internally
        self.ai = AIManager()



    @Slot(str)
    def process(self, text):

        print("=" * 60)
        print("[AIWorker] process() started")
        print(f"[AIWorker] Prompt: {text}")
        print("=" * 60)

        try:

            print("[AIWorker] Emitting LISTENING")
            self.listening.emit()


            print("[AIWorker] Running router...")
            result = self.router.route(text)

            print(f"[AIWorker] Router result: {result}")


            if result:

                print("[AIWorker] Router handled request")

                self.speaking.emit()

                self.finished.emit(result)

                return



            print("[AIWorker] Emitting THINKING")
            self.thinking.emit()


            print("[AIWorker] Calling AI Manager...")

            answer = self.ai.generate(text)


            print("[AIWorker] AI returned successfully")


            self.speaking.emit()


            print("[AIWorker] Emitting FINISHED")

            self.finished.emit(answer)


            print("[AIWorker] process() completed")



        except Exception as e:

            print("[AIWorker] ERROR")
            print(type(e).__name__)
            print(str(e))

            self.error.emit(str(e))