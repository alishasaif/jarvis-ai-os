from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)

from backend.ui.widgets.header import Header
from backend.ui.widgets.sidebar import Sidebar
from backend.ui.widgets.ai_core import AICore
from backend.ui.widgets.mission_control import MissionControl
from backend.ui.widgets.chat_panel import ChatPanel
from backend.ui.widgets.system_card import SystemCard


class Dashboard(QWidget):
    """
    Main Dashboard Layout
    """

    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)
        root.setContentsMargins(15, 15, 15, 15)
        root.setSpacing(15)

        # ======================
        # Header
        # ======================

        self.header = Header()
        root.addWidget(self.header)

        # ======================
        # Middle Layout
        # ======================

        middle = QHBoxLayout()

        self.sidebar = Sidebar()
        self.ai_core = AICore()
        self.mission = MissionControl()

        middle.addWidget(self.sidebar)
        middle.addStretch()
        middle.addWidget(self.ai_core, 1)
        middle.addStretch()
        middle.addWidget(self.mission)

        root.addLayout(middle)

        # ======================
        # System Cards
        # ======================

        cards = QGridLayout()

        self.cpu = SystemCard("CPU")
        self.ram = SystemCard("RAM")
        self.disk = SystemCard("DISK")
        self.network = SystemCard("NETWORK")
        self.battery = SystemCard("BATTERY")
        self.gpu = SystemCard("GPU")

        cards.addWidget(self.cpu, 0, 0)
        cards.addWidget(self.ram, 0, 1)
        cards.addWidget(self.disk, 0, 2)
        cards.addWidget(self.network, 1, 0)
        cards.addWidget(self.battery, 1, 1)
        cards.addWidget(self.gpu, 1, 2)

        root.addLayout(cards)

        # ======================
        # Chat
        # ======================

        self.chat = ChatPanel()

        root.addWidget(self.chat)