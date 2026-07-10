from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import QTimer

from frontend.widgets.glass_panel import GlassPanel


class RightPanel(GlassPanel):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget{
                background:#10151C;
                border:1px solid #00D8FF;
                border-radius:10px;
            }

            QLabel{
                color:#00D8FF;
                font-size:15px;
                padding:4px;
            }
        """)

        layout = QVBoxLayout()

        title = QLabel("VOICE AI")

        self.mic = QLabel("🎤 Microphone : Ready")
        self.ai = QLabel("🤖 AI : Online")
        self.speaker = QLabel("🔊 Speaker : Connected")
        self.user = QLabel("👤 User : Saif")

        layout.addWidget(title)
        layout.addSpacing(10)

        layout.addWidget(self.mic)
        layout.addWidget(self.ai)
        layout.addWidget(self.speaker)
        layout.addWidget(self.user)

        layout.addStretch()

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.demo_status)
        self.timer.start(3000)

        self.state = 0

    def demo_status(self):

        states = [
            "🎤 Microphone : Ready",
            "🎤 Listening...",
            "🧠 Thinking...",
            "🗣 Speaking..."
        ]

        self.mic.setText(states[self.state])

        self.state += 1

        if self.state >= len(states):
            self.state = 0