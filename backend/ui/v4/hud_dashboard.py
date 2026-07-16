from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from PySide6.QtCore import QTimer


from backend.services.system_service import SystemService

from backend.ui.widgets.ai_core import AICore
from backend.ui.widgets.chat_panel import ChatPanel

from backend.ui.v4.hud_panel import HUDPanel
from backend.ui.v4.status_bar import StatusBar
from backend.ui.v4.hud_label import HUDLabel



class HUDDashboard(QWidget):

    def __init__(self):

        super().__init__()


        root = QVBoxLayout(self)


        root.setContentsMargins(
            15,
            15,
            15,
            15
        )

        root.setSpacing(
            12
        )



        # =========================
        # MAIN HUD AREA
        # =========================

        center = QHBoxLayout()

        center.setSpacing(
            15
        )



        # =========================
        # LEFT SYSTEM PANEL
        # =========================


        left = HUDPanel()


        left_layout = left.layout()



        left_layout.addWidget(
            HUDLabel("SYSTEM CORE")
        )



        self.online_label = HUDLabel(
            "● ONLINE"
        )

        left_layout.addWidget(
            self.online_label
        )



        self.cpu_label = HUDLabel(
            "CPU -- %"
        )

        left_layout.addWidget(
            self.cpu_label
        )



        self.ram_label = HUDLabel(
            "RAM -- %"
        )

        left_layout.addWidget(
            self.ram_label
        )



        self.disk_label = HUDLabel(
            "DISK -- %"
        )

        left_layout.addWidget(
            self.disk_label
        )



        self.battery_label = HUDLabel(
            "BATTERY --"
        )

        left_layout.addWidget(
            self.battery_label
        )



        self.network_label = HUDLabel(
            "NETWORK --"
        )

        left_layout.addWidget(
            self.network_label
        )



        self.device_label = HUDLabel(
            "DEVICE --"
        )

        left_layout.addWidget(
            self.device_label
        )



        self.os_label = HUDLabel(
            "OS --"
        )

        left_layout.addWidget(
            self.os_label
        )



        self.uptime_label = HUDLabel(
            "UPTIME --"
        )

        left_layout.addWidget(
            self.uptime_label
        )



        self.gpu_label = HUDLabel(
            "GPU --"
        )

        left_layout.addWidget(
            self.gpu_label
        )



        left_layout.addWidget(
            HUDLabel("VOICE READY")
        )



        left_layout.addWidget(
            HUDLabel("AI STATE: IDLE")
        )




        # =========================
        # ARC REACTOR
        # =========================


        reactor = AICore()




        # =========================
        # RIGHT MISSION PANEL
        # =========================


        right = HUDPanel()


        right_layout = right.layout()



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




        center.addWidget(
            left,
            1
        )


        center.addWidget(
            reactor,
            2
        )


        center.addWidget(
            right,
            1
        )



        root.addLayout(
            center
        )



        # =========================
        # TELEMETRY
        # =========================


        self.status = StatusBar()

        root.addWidget(
            self.status
        )




        # =========================
        # CHAT TERMINAL
        # =========================


        self.chat = ChatPanel()

        root.addWidget(
            self.chat,
            2
        )




        # =========================
        # LIVE UPDATE ENGINE
        # =========================


        self.timer = QTimer()


        self.timer.timeout.connect(
            self.update_system
        )


        self.timer.start(
            2000
        )


        self.update_system()




    # =========================
    # SYSTEM DATA UPDATE
    # =========================


    def update_system(self):


        stats = SystemService.get_stats()



        self.cpu_label.setText(
            f"CPU   {stats['cpu']} %"
        )


        self.ram_label.setText(
            f"RAM   {stats['ram']} %"
        )


        self.disk_label.setText(
            f"DISK  {stats['disk']} %"
        )


        self.battery_label.setText(
            f"BATTERY  {stats['battery']}"
        )


        self.network_label.setText(
            f"NETWORK  {stats['network']}"
        )


        self.device_label.setText(
            f"DEVICE  {stats['device']}"
        )


        self.os_label.setText(
            f"OS  {stats['os']}"
        )


        self.uptime_label.setText(
            f"UPTIME  {stats['uptime']}"
        )


        self.gpu_label.setText(
            f"GPU  {stats['gpu']}"
        )