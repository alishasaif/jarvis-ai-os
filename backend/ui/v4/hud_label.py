from PySide6.QtWidgets import QLabel


class HUDLabel(QLabel):

    def __init__(self, text):
        super().__init__(text)

        self.setStyleSheet("""
        QLabel {
            color:#FFB347;
            font-size:14px;
            padding:6px;
            background:transparent;
        }
        """)
