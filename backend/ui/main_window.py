from PySide6.QtWidgets import QMainWindow

from backend.core.config import (
    APP_NAME,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from backend.ui.dashboard import Dashboard


class MainWindow(QMainWindow):
    """
    Main Application Window

    This class only manages the top-level window.
    All UI is handled by Dashboard.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.dashboard = Dashboard()

        self.setCentralWidget(self.dashboard)

        self.statusBar().showMessage(
            "READY | Voice: Idle | AI: Offline | Memory: 0"
        )