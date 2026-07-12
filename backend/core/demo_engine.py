from PySide6.QtCore import QObject, QTimer

from backend.core.app_state import app_state, AIState


class DemoEngine(QObject):

    def __init__(self):
        super().__init__()

        self.states = [
            AIState.IDLE,
            AIState.LISTENING,
            AIState.THINKING,
            AIState.SPEAKING,
        ]

        self.index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_state)

    def start(self):
        self.timer.start(3000)

    def next_state(self):

        app_state.set_state(self.states[self.index])

        self.index += 1

        if self.index >= len(self.states):
            self.index = 0