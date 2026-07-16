from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtCore import Qt


class HUDPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("HUDPanel")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10,10,10,10)

        self.setStyleSheet("""
        QFrame#HUDPanel {
            background-color: rgba(10,15,25,220);
            border: 1px solid #FF9A1F;
            border-radius: 12px;
        }
        """)

