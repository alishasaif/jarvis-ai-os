from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
)


class Header(QWidget):
    """
    Top Header Widget
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("Header")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)

        # -----------------------
        # Left Section
        # -----------------------

        left = QVBoxLayout()

        self.title = QLabel("J.A.R.V.I.S AI OS")
        self.title.setObjectName("HeaderTitle")

        self.subtitle = QLabel("Artificial Intelligence Operating System")
        self.subtitle.setObjectName("HeaderSubtitle")

        left.addWidget(self.title)
        left.addWidget(self.subtitle)

        # -----------------------
        # Right Section
        # -----------------------

        right = QVBoxLayout()

        self.status = QLabel("● AI OFFLINE")
        self.status.setAlignment(Qt.AlignRight)
        self.status.setObjectName("HeaderStatus")

        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignRight)
        self.clock.setObjectName("HeaderClock")

        right.addWidget(self.status)
        right.addWidget(self.clock)

        layout.addLayout(left)
        layout.addStretch()
        layout.addLayout(right)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.update_clock()

    def update_clock(self):
        now = datetime.now()

        self.clock.setText(
            now.strftime("%d %b %Y  |  %I:%M:%S %p")
        )

    def set_status(self, text: str):
        self.status.setText(text)