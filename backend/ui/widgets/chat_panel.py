from datetime import datetime

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)

from PySide6.QtCore import Slot

from backend.ai.controller import AIController


class ChatPanel(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = AIController()

        layout = QVBoxLayout(self)

        self.history = QTextEdit()
        self.history.setReadOnly(True)

        layout.addWidget(self.history)

        bottom = QHBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText(
            "Ask J.A.R.V.I.S..."
        )

        self.send = QPushButton("Send")

        bottom.addWidget(self.input)
        bottom.addWidget(self.send)

        layout.addLayout(bottom)

        self.send.clicked.connect(
            self.send_message
        )

        self.input.returnPressed.connect(
            self.send_message
        )

        self.controller.response_ready.connect(
            self.on_response
        )

        self.controller.error.connect(
            self.on_error
        )

        self.system_message(
            "J.A.R.V.I.S Online."
        )

        self.system_message(
            "Awaiting your command..."
        )

    def timestamp(self):

        return datetime.now().strftime(
            "%H:%M:%S"
        )

    def user_message(self, text):

        text = str(text)

        self.history.append(
            f'<span style="color:white;">'
            f'[{self.timestamp()}] YOU:</span> {text}'
        )

    def system_message(self, text):

        text = str(text)

        self.history.append(
            f'<span style="color:#00E5FF;">'
            f'[{self.timestamp()}] JARVIS:</span> {text}'
        )

        self.history.verticalScrollBar().setValue(
            self.history.verticalScrollBar().maximum()
        )

    @Slot()
    def send_message(self):

        text = self.input.text().strip()

        if not text:
            return

        if self.controller.busy:
            return

        self.user_message(text)

        self.input.clear()

        self.input.setEnabled(False)
        self.send.setEnabled(False)

        self.system_message(
            "Thinking..."
        )

        self.controller.ask(text)

    @Slot(str)
    def on_response(self, answer):

        self.system_message(
            str(answer)
        )

        self.input.setEnabled(True)
        self.send.setEnabled(True)

        self.input.setFocus()

    @Slot(str)
    def on_error(self, message):

        self.system_message(
            f"AI Error: {str(message)}"
        )

        self.input.setEnabled(True)
        self.send.setEnabled(True)

        self.input.setFocus()