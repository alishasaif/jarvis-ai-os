from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from backend.ui.widgets.ai_core import AICore
from backend.ui.widgets.chat_panel import ChatPanel

from backend.ui.v4.hud_panel import HUDPanel
from backend.ui.v4.status_bar import StatusBar
from backend.ui.v4.hud_label import HUDLabel


class HUDDashboard(QWidget):

    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)

        root.setContentsMargins(15, 15, 15, 15)
        root.setSpacing(12)

        # =========================
        # MAIN HUD AREA
        # =========================

        center = QHBoxLayout()
        center.setSpacing(15)

        # LEFT SYSTEM PANEL
        left = HUDPanel()

        left_layout = QVBoxLayout(left)

        left_layout.addWidget(
            HUDLabel("SYSTEM CORE")
        )

        left_layout.addWidget(
            HUDLabel("● ONLINE")
        )

        left_layout.addWidget(
            HUDLabel("CPU   -- %")
        )

        left_layout.addWidget(
            HUDLabel("RAM   -- %")
        )

        left_layout.addWidget(
            HUDLabel("DISK  -- %")
        )

        left_layout.addWidget(
            HUDLabel("VOICE READY")
        )

        left_layout.addWidget(
            HUDLabel("AI STATE: IDLE")
        )


        # REACTOR

        reactor = AICore()


        # RIGHT MISSION PANEL

        right = HUDPanel()

        right_layout = QVBoxLayout(right)

        right_layout.addWidget(
            HUDLabel("MISSION CONTROL")
        )

        right_layout.addWidget(
            HUDLabel("AI ENGINE ONLINE")
        )

        right_layout.addWidget(
            HUDLabel("MODEL: JARVIS LOCAL")
        )

        right_layout.addWidget(
            HUDLabel("OLLAMA CONNECTED")
        )

        right_layout.addWidget(
            HUDLabel("MEMORY READY")
        )

        right_layout.addWidget(
            HUDLabel("COMMANDS READY")
        )


        center.addWidget(left, 1)
        center.addWidget(reactor, 2)
        center.addWidget(right, 1)

        root.addLayout(center)


        # =========================
        # TELEMETRY
        # =========================

        self.status = StatusBar()
        root.addWidget(self.status)


        # =========================
        # TERMINAL
        # =========================

        self.chat = ChatPanel()
        root.addWidget(self.chat, 2)
