from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import QTimer

import psutil



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



        # Live labels

        self.cpu = QLabel()

        self.ram = QLabel()

        self.disk = QLabel()

        self.battery = QLabel()

        self.network = QLabel()



        labels = [
            self.cpu,
            self.ram,
            self.disk,
            self.battery,
            self.network
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


        self.setLayout(
            layout
        )


        self.setFixedWidth(
            260
        )



        # Update every second

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.update_system
        )

        self.timer.start(1000)



        self.update_system()



    def update_system(self):


        # CPU

        cpu = psutil.cpu_percent()


        self.cpu.setText(
            f"CPU : {cpu}%"
        )



        # RAM

        ram = psutil.virtual_memory()


        self.ram.setText(
            f"RAM : {ram.percent}%"
        )



        # Disk

        disk = psutil.disk_usage("/")


        self.disk.setText(
            f"DISK : {disk.percent}%"
        )



        # Battery

        battery = psutil.sensors_battery()


        if battery:

            self.battery.setText(
                f"BATTERY : {battery.percent}%"
            )

        else:

            self.battery.setText(
                "BATTERY : N/A"
            )



        # Network

        net = psutil.net_io_counters()


        sent = round(
            net.bytes_sent / (1024*1024),
            2
        )


        recv = round(
            net.bytes_recv / (1024*1024),
            2
        )


        self.network.setText(
            f"NETWORK ↑{sent}MB ↓{recv}MB"
        )