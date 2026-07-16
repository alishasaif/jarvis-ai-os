from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from PySide6.QtCore import QTimer


from backend.services.system_service import SystemService

from backend.ui.widgets.ai_core import AICore
from backend.ui.widgets.chat_panel import ChatPanel
from backend.ui.widgets.system_gauge import SystemGauge

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



        # =========================
        # JARVIS SYSTEM GAUGES
        # =========================


        self.cpu_gauge = SystemGauge(
            "CPU"
        )


        self.ram_gauge = SystemGauge(
            "RAM"
        )


        self.disk_gauge = SystemGauge(
            "DISK"
        )


        left_layout.addWidget(
            self.cpu_gauge
        )


        left_layout.addWidget(
            self.ram_gauge
        )


        left_layout.addWidget(
            self.disk_gauge
        )



        # =========================
        # EXTRA TELEMETRY
        # =========================


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
        # TELEMETRY BAR
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



        # GAUGES

        self.cpu_gauge.setValue(
            stats["cpu"]
        )


        self.ram_gauge.setValue(
            stats["ram"]
        )


        self.disk_gauge.setValue(
            stats["disk"]
        )



        # TEXT TELEMETRY


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