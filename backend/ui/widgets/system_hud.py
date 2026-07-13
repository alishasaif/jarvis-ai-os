from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout


class HUDItem(QLabel):

    def __init__(self, title):
        super().__init__()

        self.title = title

        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""
            QLabel{
                background:#10151d;
                border:1px solid #00d9ff;
                border-radius:8px;
                color:#00e5ff;
                font-size:13px;
                font-weight:bold;
                padding:8px;
            }
        """)

        self.update_value("--")

    def update_value(self, value):
        self.setText(f"{self.title}\n{value}")


class SystemHUD(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(8)

        self.cpu = HUDItem("CPU")
        self.ram = HUDItem("RAM")
        self.disk = HUDItem("DISK")
        self.net = HUDItem("NET")
        self.gpu = HUDItem("GPU")
        self.battery = HUDItem("BAT")

        layout.addWidget(self.cpu)
        layout.addWidget(self.ram)
        layout.addWidget(self.disk)
        layout.addWidget(self.net)
        layout.addWidget(self.gpu)
        layout.addWidget(self.battery)

    def update(self, stats):

        self.cpu.update_value(f"{stats['cpu']}%")
        self.ram.update_value(f"{stats['ram']}%")
        self.disk.update_value(f"{stats['disk']}%")
        self.net.update_value(stats["network"])
        self.gpu.update_value(stats["gpu"])
        self.battery.update_value(stats["battery"])