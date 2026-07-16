from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout


class StatusBar(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        self.cpu = QLabel("CPU 0%")
        self.ram = QLabel("RAM 0%")
        self.disk = QLabel("DISK 0%")
        self.net = QLabel("NET 0 MB")

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

