from PySide6.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

from backend.ui import theme


class HUDPanel(QFrame):
    """
    Base holographic panel used throughout J.A.R.V.I.S.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("HUDPanel")

        glow = QGraphicsDropShadowEffect(self)
        glow.setBlurRadius(25)
        glow.setOffset(0, 0)
        glow.setColor(QColor(theme.PRIMARY))

        self.setGraphicsEffect(glow)

        self.setStyleSheet(f"""
        QFrame#HUDPanel{{
            background-color:{theme.PANEL};
            border:1px solid {theme.BORDER};
            border-radius:18px;
        }}

        QFrame#HUDPanel:hover{{
            border:2px solid {theme.PRIMARY};
        }}
        """)
