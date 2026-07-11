from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QColor
import random


class Waveform(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumHeight(120)
        self.setMinimumWidth(250)

        self.bars = [random.randint(10, 60) for _ in range(24)]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(80)

    def animate(self):

        self.bars = [
            random.randint(10, 70)
            for _ in self.bars
        ]

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()

        spacing = width / len(self.bars)

        for i, value in enumerate(self.bars):

            x = i * spacing + 2

            y = (height - value) / 2

            painter.setBrush(QColor(0, 216, 255))
            painter.setPen(QColor(0, 216, 255))

            painter.drawRoundedRect(
                int(x),
                int(y),
                6,
                value,
                3,
                3
            )