from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("J.A.R.V.I.S AI OS")
        self.resize(1600, 900)

        self.setStyleSheet("""
            QMainWindow{
                background:#05070B;
            }

            QLabel{
                color:#00D8FF;
            }
        """)

        title = QLabel("J.A.R.V.I.S", self)
        title.setAlignment(Qt.AlignCenter)

        font = QFont("Segoe UI", 34)
        font.setBold(True)

        title.setFont(font)

        self.setCentralWidget(title)