from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedLayout,
)
from PySide6.QtCore import Qt

from frontend.components.header import Header
from frontend.components.left_panel import LeftPanel
from frontend.components.right_panel import RightPanel

from frontend.widgets.arc_reactor import ArcReactor
from frontend.widgets.particle_background import ParticleBackground


class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("J.A.R.V.I.S AI OS")
        self.resize(1600, 900)

        self.setStyleSheet("""
            QMainWindow{
                background:#05070B;
            }
        """)

        # Root widget
        root = QWidget()
        self.setCentralWidget(root)

        # Stack layout (background + foreground)
        stack = QStackedLayout(root)
        stack.setStackingMode(QStackedLayout.StackAll)

        # Background
        background = ParticleBackground()

        # Foreground
        foreground = QWidget()

        main_layout = QVBoxLayout(foreground)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # Header
        main_layout.addWidget(Header())

        # Body
        body = QHBoxLayout()
        body.setSpacing(20)

        # Left Panel
        body.addWidget(LeftPanel(), 1)

        # AI Core
        ai_core = ArcReactor()
        body.addWidget(ai_core, 2, Qt.AlignmentFlag.AlignCenter)

        # Right Panel
        body.addWidget(RightPanel(), 1)

        main_layout.addLayout(body)

        # Add to stack
        stack.addWidget(background)
        stack.addWidget(foreground)