from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("J.A.R.V.I.S AI OS")

        self.resize(1600, 900)

        self.setStyleSheet("""
            QMainWindow{
                background-color:#070b14;
            }

            QLabel{
                color:#00E5FF;
            }
        """)

        label = QLabel("J.A.R.V.I.S", self)
        label.setAlignment(Qt.AlignCenter)

        font = QFont("Segoe UI", 38)
        font.setBold(True)

        label.setFont(font)

        self.setCentralWidget(label)