from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QListWidget, QListWidgetItem


class Sidebar(QListWidget):
    """
    Left Navigation Panel
    """

    page_changed = Signal(object)

    def __init__(self):
        super().__init__()

        self.setObjectName("Sidebar")

        self.setMinimumWidth(240)
        self.setMaximumWidth(260)

        self.setSpacing(6)
        self.setAlternatingRowColors(False)

        pages = [
            ("🏠", "Dashboard"),
            ("💬", "Chat"),
            ("🧠", "Memory"),
            ("🤖", "AI Models"),
            ("🎤", "Voice"),
            ("⚡", "Automation"),
            ("📱", "Android"),
            ("🔌", "Plugins"),
            ("⚙", "Settings"),
        ]

        for icon, name in pages:
            item = QListWidgetItem(f"{icon}   {name}")
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.addItem(item)

        self.setCurrentRow(0)

        self.currentTextChanged.connect(self.on_page_changed)

    def on_page_changed(self, text):
        self.page_changed.emit(text)