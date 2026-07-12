from PySide6.QtCore import QObject, Signal


class AIStateManager(QObject):

    state_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.state = "IDLE"


    def set_state(self, state):

        self.state = state.upper()

        self.state_changed.emit(self.state)


    def get_state(self):

        return self.state