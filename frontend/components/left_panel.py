from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer

from backend.services.system_monitor import SystemMonitor


class LeftPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.monitor = SystemMonitor()

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

        self.title = QLabel("SYSTEM STATUS")

        self.cpu = QLabel()
        self.ram = QLabel()
        self.disk = QLabel()
        self.network = QLabel()
        self.uptime = QLabel()

        layout.addWidget(self.title)
        layout.addSpacing(10)

        layout.addWidget(self.cpu)
        layout.addWidget(self.ram)
        layout.addWidget(self.disk)
        layout.addWidget(self.network)
        layout.addWidget(self.uptime)

        layout.addStretch()

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

        self.update_stats()

    def update_stats(self):

        self.cpu.setText(
            f"CPU : {self.monitor.get_cpu()} %"
        )

        self.ram.setText(
            f"RAM : {self.monitor.get_ram()} %"
        )

        self.disk.setText(
            f"DISK : {self.monitor.get_disk()} %"
        )

        self.network.setText(
            f"NETWORK : {self.monitor.get_network_status()}"
        )

        self.uptime.setText(
            f"UPTIME : {self.monitor.get_uptime()}"
        )