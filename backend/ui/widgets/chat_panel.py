from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)


class ChatPanel(QWidget):
    """
    Chat Console Widget
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("ChatPanel")

        layout = QVBoxLayout(self)

        # Chat History
        self.history = QTextEdit()
        self.history.setReadOnly(True)

        layout.addWidget(self.history)

        # Input Row
        bottom = QHBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Type a command...")

        self.send = QPushButton("Send")

        bottom.addWidget(self.input)
        bottom.addWidget(self.send)

        layout.addLayout(bottom)

        self.send.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

        self.system_message("J.A.R.V.I.S initialized.")
        self.system_message("Awaiting your command...")

    def system_message(self, text):
        time = datetime.now().strftime("%H:%M:%S")
        self.history.append(
            f'<span style="color:#00E5FF;">[{time}] JARVIS:</span> {text}'
        )

    def user_message(self, text):
        time = datetime.now().strftime("%H:%M:%S")
        self.history.append(
            f'<span style="color:#FFFFFF;">[{time}] YOU:</span> {text}'
        )

    def send_message(self):
        text = self.input.text().strip()

        if not text:
            return

        self.user_message(text)

        # Placeholder response
        self.system_message("Processing request...")

        self.input.clear()