from PySide6.QtWidgets import QMainWindow

from backend.ui.v4.hud_dashboard import HUDDashboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("J.A.R.V.I.S AI OS")

        self.resize(1700, 950)

        self.setCentralWidget(HUDDashboard())
