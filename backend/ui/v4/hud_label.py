from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class HUDLabel(QLabel):

    def __init__(self, text: str = ""):

        super().__init__()

        self.setText(text)

        self.setAlignment(
            Qt.AlignLeft | Qt.AlignVCenter
        )

        self.setStyleSheet("""
        QLabel {
            color:#FFB347;
            font-size:14px;
            padding:6px;
            background:transparent;
        }
        """)