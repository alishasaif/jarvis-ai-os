from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout


class StatusBar(QWidget):

    def __init__(self):

        super().__init__()


        layout = QHBoxLayout(self)


        self.cpu = QLabel(
            "CPU 0%"
        )

        self.ram = QLabel(
            "RAM 0%"
        )

        self.disk = QLabel(
            "DISK 0%"
        )

        self.net = QLabel(
            "NET 0 MB"
        )


        for item in [
            self.cpu,
            self.ram,
            self.disk,
            self.net
        ]:

            layout.addWidget(item)



        self.setStyleSheet("""
        QLabel {
            color:#FFB347;
            font-size:14px;
            padding:8px;
            border:1px solid #7A4A11;
            border-radius:8px;
            background:#050505;
        }
        """)



    def update_cpu(self, value):

        self.cpu.setText(
            f"CPU {str(value)}%"
        )



    def update_ram(self, value):

        self.ram.setText(
            f"RAM {str(value)}%"
        )



    def update_disk(self, value):

        self.disk.setText(
            f"DISK {str(value)}%"
        )



    def update_network(self, value):

        self.net.setText(
            f"NET {str(value)}"
        )