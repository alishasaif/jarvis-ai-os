from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from PySide6.QtCore import QTimer

from backend.services.system_service import SystemService
from backend.core.jarvis_events import jarvis_events

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
        # SYSTEM GAUGES
        # =========================

        self.cpu_gauge = SystemGauge("CPU")

        self.ram_gauge = SystemGauge("RAM")

        self.disk_gauge = SystemGauge("DISK")

        gauge_box = QHBoxLayout()

        gauge_box.setSpacing(
            15
        )

        gauge_box.addWidget(
            self.cpu_gauge
        )

        gauge_box.addWidget(
            self.ram_gauge
        )

        gauge_box.addWidget(
            self.disk_gauge
        )

        left_layout.addLayout(
            gauge_box
        )

        # =========================
        # TELEMETRY
        # =========================

        self.battery_label = HUDLabel(
            "BATTERY --"
        )

        self.network_label = HUDLabel(
            "NETWORK --"
        )

        self.device_label = HUDLabel(
            "DEVICE --"
        )

        self.os_label = HUDLabel(
            "OS --"
        )

        self.uptime_label = HUDLabel(
            "UPTIME --"
        )

        self.gpu_label = HUDLabel(
            "GPU --"
        )

        for label in [
            self.battery_label,
            self.network_label,
            self.device_label,
            self.os_label,
            self.uptime_label,
            self.gpu_label
        ]:

            left_layout.addWidget(
                label
            )

        left_layout.addWidget(
            HUDLabel("VOICE READY")
        )

        self.ai_state_label = HUDLabel(
            "AI STATE: IDLE"
        )

        left_layout.addWidget(
            self.ai_state_label
        )

        # =========================
        # ARC REACTOR
        # =========================

        self.reactor = AICore()

        jarvis_events.state_changed.connect(
            self.update_ai_state
        )

        jarvis_events.state_changed.connect(
            self.reactor.set_state
        )

        # =========================
        # SYSTEM EVENT BUS
        # =========================

        jarvis_events.system_updated.connect(
            self.on_system_update
        )

        # =========================
        # RIGHT MISSION PANEL
        # =========================

        right = HUDPanel()

        right_layout = right.layout()

        right_layout.addWidget(
            HUDLabel("MISSION CONTROL")
        )

        self.ai_engine_label = HUDLabel(
            "AI ENGINE : ACTIVE"
        )

        right_layout.addWidget(
            self.ai_engine_label
        )

        self.model_label = HUDLabel(
            "MODEL : qwen3-coder:30b"
        )

        right_layout.addWidget(
            self.model_label
        )

        self.ollama_label = HUDLabel(
            "OLLAMA : CONNECTED"
        )

        right_layout.addWidget(
            self.ollama_label
        )

        self.memory_label = HUDLabel(
            "MEMORY : READY"
        )

        right_layout.addWidget(
            self.memory_label
        )

        self.voice_label = HUDLabel(
            "VOICE : READY"
        )

        right_layout.addWidget(
            self.voice_label
        )

        self.command_label = HUDLabel(
            "LAST COMMAND : NONE"
        )

        right_layout.addWidget(
            self.command_label
        )

        center.addWidget(
            left,
            2
        )

        center.addWidget(
            self.reactor,
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
        # STATUS BAR
        # =========================

        self.status = StatusBar()

        root.addWidget(
            self.status
        )

        # =========================
        # CHAT
        # =========================

        self.chat = ChatPanel()

        root.addWidget(
            self.chat,
            2
        )

        # =========================
        # LIVE UPDATE TIMER
        # =========================

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.update_system
        )

        self.timer.start(
            2000
        )

        self.update_system()

    # =========================
    # AI STATE UPDATE
    # =========================

    def update_ai_state(self, state):

        self.ai_state_label.setText(
            f"AI STATE: {state}"
        )

    # =========================
    # TIMER
    # =========================

    def update_system(self):

        SystemService.publish_stats()

    # =========================
    # EVENT BUS CALLBACK
    # =========================

    def on_system_update(self, stats):

        self.cpu_gauge.setValue(
            stats["cpu"]
        )

        self.ram_gauge.setValue(
            stats["ram"]
        )

        self.disk_gauge.setValue(
            stats["disk"]
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