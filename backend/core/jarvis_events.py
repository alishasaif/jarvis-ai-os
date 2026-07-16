from PySide6.QtCore import QObject, Signal


class JarvisEvents(QObject):

    state_changed = Signal(str)


jarvis_events = JarvisEvents()