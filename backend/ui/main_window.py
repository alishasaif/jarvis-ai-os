from PySide6.QtWidgets import QMainWindow

from frontend.windows.dashboard import Dashboard


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "J.A.R.V.I.S AI OS"
        )

        self.resize(
            1700,
            950
        )

        self.setCentralWidget(
            Dashboard()
        )