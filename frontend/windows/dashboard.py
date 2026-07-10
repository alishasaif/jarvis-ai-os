from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from frontend.components.header import Header
from frontend.components.left_panel import LeftPanel


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

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        main_layout.addWidget(Header())

        body = QHBoxLayout()

        body.addWidget(LeftPanel(), 1)

        body.addStretch(4)

        main_layout.addLayout(body)

        central.setLayout(main_layout)

        self.setCentralWidget(central)