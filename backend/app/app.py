from PySide6.QtWidgets import QApplication

import sys

from frontend.windows.dashboard import Dashboard



def run():

    app = QApplication(sys.argv)


    window = Dashboard()

    window.show()


    sys.exit(
        app.exec()
    )