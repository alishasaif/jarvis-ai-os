from backend.system_monitor import SystemMonitor

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtCore import Qt


from frontend.components.header import Header
from frontend.components.left_panel import LeftPanel
from frontend.components.right_panel import RightPanel

from frontend.widgets.arc_reactor import ArcReactor


class Dashboard(QMainWindow):

    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "J.A.R.V.I.S AI OS"
        )


        self.resize(
            1600,
            900
        )


        self.setStyleSheet("""
            QMainWindow{
                background:#05070B;
            }
        """)


        # Main Widget

        root = QWidget()

        self.setCentralWidget(
            root
        )


        main_layout = QVBoxLayout()


        main_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        root.setLayout(
            main_layout
        )


        # Header

        header = Header()

        main_layout.addWidget(
            header
        )


        # Center Area

        body = QHBoxLayout()


        body.setSpacing(
            30
        )


        # Left

        left = LeftPanel()

        body.addWidget(
            left
        )


        # Arc Reactor

        self.arc = ArcReactor()

        body.addWidget(
            self.arc,
            1,
            Qt.AlignmentFlag.AlignCenter
        )


        # Right

        right = RightPanel()

        body.addWidget(
            right
        )


        # LIVE SYSTEM DATA TEST

        print("===== JARVIS LIVE SYSTEM =====")

        print(
            "CPU:",
            SystemMonitor.get_cpu(),
            "%"
        )

        print(
            "RAM:",
            SystemMonitor.get_ram(),
            "%"
        )

        print(
            "DISK:",
            SystemMonitor.get_disk(),
            "%"
        )

        print(
            "DEVICE:",
            SystemMonitor.get_device()
        )

        print(
            "OS:",
            SystemMonitor.get_os()
        )

        print(
            "IP:",
            SystemMonitor.get_network()
        )


        main_layout.addLayout(
            body
        )