from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from frontend.components.header import Header


class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("J.A.R.V.I.S AI OS")

        self.resize(1600, 900)

        self.setStyleSheet("""
            QMainWindow{
                background:#05070B;
            }
        """)

        central = QWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(Header())

        central.setLayout(layout)

        self.setCentralWidget(central)