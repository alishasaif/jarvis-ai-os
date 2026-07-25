from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class HUDLabel(QLabel):

    def __init__(self, text: str = ""):

        super().__init__()

        self.setText(str(text))

        self.setAlignment(
            Qt.AlignLeft | Qt.AlignVCenter
        )

        self.setMinimumHeight(
            32
        )

        self.setStyleSheet("""
        QLabel {
            color:#FFB347;
            font-size:14px;
            padding-left:8px;
            padding-top:4px;
            padding-bottom:4px;
            background:transparent;
        }
        """)