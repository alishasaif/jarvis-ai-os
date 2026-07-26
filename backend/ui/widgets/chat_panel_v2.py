from datetime import datetime

from PySide6.QtCore import Slot
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)

from backend.ai.controller import AIController


class ChatPanelV2(QWidget):

    def __init__(self):

        super().__init__()

        self.controller = AIController()

        root = QVBoxLayout(self)

        root.setContentsMargins(
            10,
            10,
            10,
            10
        )

        root.setSpacing(10)

        self.console = QTextEdit()

        self.console.setReadOnly(True)

        self.console.setStyleSheet("""
QTextEdit{
background:#111827;
border:2px solid #1d4f91;
border-radius:14px;
color:white;
font-size:15px;
padding:12px;
}
""")

        root.addWidget(
            self.console,
            1
        )

        bottom = QHBoxLayout()

        self.input = QLineEdit()

        self.input.setPlaceholderText(
            "Ask J.A.R.V.I.S anything..."
        )

        self.input.setStyleSheet("""
QLineEdit{
background:#111827;
border:2px solid #1d4f91;
border-radius:10px;
padding:10px;
color:white;
font-size:15px;
}
""")

        self.send = QPushButton("SEND")

        self.send.setStyleSheet("""
QPushButton{
background:#00d9ff;
color:black;
font-weight:bold;
border-radius:10px;
padding:10px 18px;
}

QPushButton:hover{
background:#5ae7ff;
}
""")

        bottom.addWidget(
            self.input,
            1
        )

        bottom.addWidget(
            self.send
        )

        root.addLayout(bottom)

        self.send.clicked.connect(
            self.ask_ai
        )

        self.input.returnPressed.connect(
            self.ask_ai
        )

        self.controller.response_ready.connect(
            self.on_response
        )

        self.controller.error.connect(
            self.on_error
        )

        self.jarvis_message(
            "J.A.R.V.I.S ONLINE"
        )

        self.jarvis_message(
            "Awaiting your command."
        )

    def timestamp(self):

        return datetime.now().strftime(
            "%H:%M:%S"
        )

    def append(self, html):

        self.console.moveCursor(
            QTextCursor.End
        )

        self.console.insertHtml(html)

        self.console.insertHtml("<br><br>")

        self.console.moveCursor(
            QTextCursor.End
        )

    def user_message(self, text):

        self.append(f"""
<span style='color:#ffffff'>
[{self.timestamp()}]
<b>YOU</b>
</span><br>
{text}
""")

    def jarvis_message(self, text):

        self.append(f"""
<span style='color:#00e5ff'>
[{self.timestamp()}]
<b>JARVIS</b>
</span><br>
{text}
""")

    @Slot()
    def ask_ai(self):

        prompt = self.input.text().strip()

        if not prompt:
            return

        if self.controller.busy:
            return

        self.user_message(prompt)

        self.input.clear()

        self.input.setEnabled(False)

        self.send.setEnabled(False)

        self.jarvis_message(
            "Thinking..."
        )

        self.controller.ask(prompt)

    @Slot(str)
    def on_response(self, answer):

        self.jarvis_message(
            str(answer)
        )

        self.input.setEnabled(True)

        self.send.setEnabled(True)

        self.input.setFocus()

    @Slot(str)
    def on_error(self, error):

        self.jarvis_message(
            f"ERROR : {error}"
        )

        self.input.setEnabled(True)

        self.send.setEnabled(True)

        self.input.setFocus()