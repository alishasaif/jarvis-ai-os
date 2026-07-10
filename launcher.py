import sys

from PySide6.QtWidgets import QApplication

from frontend.windows.splash import SplashScreen


def main():

    app = QApplication(sys.argv)

    splash = SplashScreen()

    splash.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()