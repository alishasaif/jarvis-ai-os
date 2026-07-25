from PySide6.QtCore import QObject, QThread, Signal

from backend.workers.ai_worker import AIWorker
from backend.core.jarvis_events import jarvis_events



class AIController(QObject):

    response_ready = Signal(str)

    error = Signal(str)



    def __init__(self):

        super().__init__()

        self.thread = None
        self.worker = None
        self.busy = False



    def ask(self, prompt: str):


        if self.busy:
            return


        print("[AIController] ask() called")


        self.busy = True


        self.thread = QThread()


        self.worker = AIWorker()


        self.worker.moveToThread(
            self.thread
        )


        self.thread.started.connect(
            lambda:
            self.worker.process(
                str(prompt)
            )
        )


        self.worker.finished.connect(
            self._finished
        )


        self.worker.error.connect(
            self._error
        )


        self.worker.listening.connect(
            lambda:
            jarvis_events.state_changed.emit(
                "LISTENING"
            )
        )


        self.worker.thinking.connect(
            lambda:
            jarvis_events.state_changed.emit(
                "THINKING"
            )
        )


        self.worker.speaking.connect(
            lambda:
            jarvis_events.state_changed.emit(
                "SPEAKING"
            )
        )


        print("[AIController] Starting worker thread")


        self.thread.start()



    def _finished(self, text):


        self.busy = False


        jarvis_events.state_changed.emit(
            "IDLE"
        )


        self.response_ready.emit(
            str(text)
        )


        self.cleanup()



    def _error(self, message):


        self.busy = False


        jarvis_events.state_changed.emit(
            "ERROR"
        )


        self.error.emit(
            str(message)
        )


        self.cleanup()



    def cleanup(self):


        if self.thread:


            self.thread.quit()

            self.thread.wait()



        if self.worker:

            self.worker.deleteLater()



        if self.thread:

            self.thread.deleteLater()



        self.worker = None
        self.thread = None