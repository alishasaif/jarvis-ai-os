from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar,
)

from PySide6.QtCore import Qt, QTimer

from frontend.windows.dashboard import Dashboard


class SplashScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.progress = 0

        self.dashboard = None

        self.setWindowTitle("J.A.R.V.I.S")

        self.resize(700, 350)

        self.setStyleSheet("""
            QWidget{
                background:#05070B;
                color:white;
            }

            QLabel{
                color:#00D8FF;
            }

            QProgressBar{
                border:1px solid #00D8FF;
                text-align:center;
                height:20px;
            }

            QProgressBar::chunk{
                background:#00D8FF;
            }
        """)

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignCenter)

        self.title = QLabel("J.A.R.V.I.S")

        self.title.setAlignment(Qt.AlignCenter)

        self.title.setStyleSheet("font-size:34px;font-weight:bold;")

        self.status = QLabel("Initializing...")

        self.status.setAlignment(Qt.AlignCenter)

        self.bar = QProgressBar()

        layout.addWidget(self.title)
        layout.addWidget(self.status)
        layout.addWidget(self.bar)

        self.setLayout(layout)

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_progress)

        self.timer.start(40)

    def update_progress(self):

        self.progress += 1

        self.bar.setValue(self.progress)

        if self.progress < 20:
            self.status.setText("Loading Core...")

        elif self.progress < 40:
            self.status.setText("Loading Memory...")

        elif self.progress < 60:
            self.status.setText("Loading Security...")

        elif self.progress < 80:
            self.status.setText("Loading Voice Engine...")

        elif self.progress < 100:
            self.status.setText("Loading Dashboard...")

        else:

            self.timer.stop()

            self.dashboard = Dashboard()

            self.dashboard.show()

            self.close()