from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)
from PySide6.QtCore import Qt

from frontend.components.header import Header
from frontend.components.left_panel import LeftPanel
from frontend.components.right_panel import RightPanel
from frontend.widgets.animated_ring import AnimatedRing


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
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # Header
        main_layout.addWidget(Header())

        # Body
        body = QHBoxLayout()
        body.setSpacing(20)

        # Left Panel
        body.addWidget(LeftPanel(), 1)

        # Center AI Core
        ai_core = AnimatedRing()
        body.addWidget(ai_core, 2, Qt.AlignmentFlag.AlignCenter)

        # Right Voice Panel
        body.addWidget(RightPanel(), 1)

        main_layout.addLayout(body)

        central.setLayout(main_layout)

        self.setCentralWidget(central)