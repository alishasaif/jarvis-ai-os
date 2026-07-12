import sys

from PySide6.QtWidgets import QApplication

from backend.core.logger import setup_logger
from backend.ui.theme import Theme
from backend.ui.main_window import MainWindow


def run():
    setup_logger()

    app = QApplication(sys.argv)

    app.setStyleSheet(Theme.stylesheet())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())