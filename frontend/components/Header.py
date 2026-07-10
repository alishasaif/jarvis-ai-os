from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, QTimer
from datetime import datetime


class Header(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(70)

        layout = QHBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)

        self.title = QLabel("J.A.R.V.I.S AI OS")
        self.title.setStyleSheet("""
            color:#00D8FF;
            font-size:24px;
            font-weight:bold;
        """)

        self.status = QLabel("🟢 ONLINE")
        self.status.setStyleSheet("""
            color:#00FF99;
            font-size:16px;
        """)

        self.clock = QLabel()
        self.clock.setStyleSheet("""
            color:white;
            font-size:16px;
        """)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.status)
        layout.addSpacing(30)
        layout.addWidget(self.clock)

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.update_clock)
        timer.start(1000)

        self.update_clock()

    def update_clock(self):
        self.clock.setText(datetime.now().strftime("%H:%M:%S"))