from enum import Enum
from PySide6.QtCore import QObject, Signal


class AIState(Enum):
    IDLE = "Idle"
    LISTENING = "Listening"
    THINKING = "Thinking"
    SPEAKING = "Speaking"
    ERROR = "Error"


class AppStateManager(QObject):

    state_changed = Signal(object)

    def __init__(self):
        super().__init__()

        self._state = AIState.IDLE

    @property
    def state(self):
        return self._state

    def set_state(self, state):

        if state != self._state:

            self._state = state
            self.state_changed.emit(state)


app_state = AppStateManager()