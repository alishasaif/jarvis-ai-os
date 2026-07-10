from PySide6.QtWidgets import QFrame
from frontend.styles import theme


class GlassPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"""
            QFrame {{

                background-color: {theme.PANEL};

                border: 2px solid {theme.ACCENT};

                border-radius: 18px;

            }}
        """)