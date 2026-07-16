from PySide6.QtCore import QObject, Signal


class JARVISEvents(QObject):

    state_changed = Signal(str)


    def __init__(self):

        super().__init__()


    def set_state(self, state):

        self.state_changed.emit(
            state
        )


# Global Event Bus

jarvis_events = JARVISEvents()