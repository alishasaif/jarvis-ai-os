from datetime import datetime

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)

from backend.ai.router import AIRouter
from backend.ai.providers.ollama_provider import OllamaProvider


class ChatPanel(QWidget):
    """
    J.A.R.V.I.S Chat Panel
    """

    def __init__(self):
        super().__init__()

        self.router = AIRouter()
        self.ai = OllamaProvider()

        layout = QVBoxLayout(self)

        # Chat History
        self.history = QTextEdit()
        self.history.setReadOnly(True)

        layout.addWidget(self.history)

        # Bottom Input
        bottom = QHBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Ask J.A.R.V.I.S...")

        self.send = QPushButton("Send")

        bottom.addWidget(self.input)
        bottom.addWidget(self.send)

        layout.addLayout(bottom)

        self.send.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

        self.system_message("J.A.R.V.I.S Online.")
        self.system_message("Awaiting your command...")

    def timestamp(self):
        return datetime.now().strftime("%H:%M:%S")

    def user_message(self, text):
        self.history.append(
            f'<span style="color:white;">[{self.timestamp()}] YOU:</span> {text}'
        )

    def system_message(self, text):
        self.history.append(
            f'<span style="color:#00E5FF;">[{self.timestamp()}] JARVIS:</span> {text}'
        )

    def send_message(self):

        text = self.input.text().strip()

        if not text:
            return

        self.user_message(text)
        self.input.clear()

        # Try local command first
        result = self.router.route(text)

        if result:
            self.system_message(result)
            return

        # Otherwise ask Ollama
        try:
            answer = self.ai.generate(text)
            self.system_message(answer)

        except Exception as e:
            self.system_message(f"AI Error: {e}")