from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)

from backend.ui import theme


class SystemCard(QFrame):
    """
    J.A.R.V.I.S HUD System Card
    """

    def __init__(self, title: str, value: str = "--"):
        super().__init__()

        self.setObjectName("SystemCard")

        self.setMinimumHeight(105)
        self.setMaximumHeight(115)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 12, 18, 12)
        layout.setSpacing(6)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet(f"""
            QLabel {{
                color: {theme.TEXT_SECONDARY};
                font-size: 15px;
                font-weight: bold;
                letter-spacing: 2px;
            }}
        """)

        self.value = QLabel(value)
        self.value.setAlignment(Qt.AlignCenter)

        self.value.setStyleSheet(f"""
            QLabel {{
                color: {theme.PRIMARY_LIGHT};
                font-size: 26px;
                font-weight: bold;
            }}
        """)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

        self.setStyleSheet(f"""
            QFrame#SystemCard {{
                background-color: {theme.PANEL};
                border: 1px solid {theme.BORDER};
                border-radius: 12px;
            }}

            QFrame#SystemCard:hover {{
                border: 2px solid {theme.PRIMARY};
            }}
        """)

    def set_value(self, value):
        self.value.setText(str(value))