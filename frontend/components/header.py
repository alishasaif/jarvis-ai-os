from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt


class Header(QWidget):

    def __init__(self):

        super().__init__()


        layout = QHBoxLayout()


        title = QLabel(
            "J.A.R.V.I.S  AI OS"
        )


        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        title.setStyleSheet("""
            QLabel{
                color:#00d8ff;
                font-size:28px;
                font-weight:bold;
                letter-spacing:3px;
            }
        """)


        layout.addWidget(
            title
        )


        self.setLayout(
            layout
        )