from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import QTimer

from backend.services.system_service import SystemService


class LeftPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel(
            "SYSTEM MONITOR"
        )

        title.setStyleSheet("""
            QLabel{
                color:#00d8ff;
                font-size:18px;
                font-weight:bold;
            }
        """)

        layout.addWidget(title)


        self.cpu = QLabel()
        self.ram = QLabel()
        self.disk = QLabel()
        self.battery = QLabel()
        self.network = QLabel()
        self.gpu = QLabel()
        self.uptime = QLabel()


        labels = [
            self.cpu,
            self.ram,
            self.disk,
            self.gpu,
            self.battery,
            self.network,
            self.uptime
        ]


        for item in labels:

            item.setStyleSheet("""
                QLabel{
                    color:#9eeaff;
                    font-size:14px;
                    padding:8px;
                    border:1px solid #003344;
                    border-radius:6px;
                }
            """)

            layout.addWidget(item)



        layout.addStretch()


        self.setLayout(layout)


        self.setFixedWidth(260)



        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.update_system
        )

        self.timer.start(1000)


        self.update_system()



    def update_system(self):

        stats = SystemService.get_stats()


        self.cpu.setText(
            f"CPU : {stats['cpu']}%"
        )


        self.ram.setText(
            f"RAM : {stats['ram']}%"
        )


        self.disk.setText(
            f"DISK : {stats['disk']}%"
        )


        self.gpu.setText(
            f"GPU : {stats['gpu']}"
        )


        self.battery.setText(
            f"BATTERY : {stats['battery']}"
        )


        self.network.setText(
            f"NETWORK : {stats['network']}"
        )


        self.uptime.setText(
            f"UPTIME : {stats['uptime']}"
        )