from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class SystemCard(QFrame):
    """
    Reusable System Information Card
    """

    def __init__(self, title: str, value: str = "--"):
        super().__init__()

        self.setObjectName("SystemCard")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        self.title = QLabel(title)
        self.title.setObjectName("SystemCardTitle")
        self.title.setAlignment(Qt.AlignCenter)

        self.value = QLabel(value)
        self.value.setObjectName("SystemCardValue")
        self.value.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

    def set_value(self, value):
        """
        Update the displayed value.
        """
        self.value.setText(str(value))