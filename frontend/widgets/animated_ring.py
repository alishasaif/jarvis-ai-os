from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QColor, QPen
import math


class AnimatedRing(QWidget):

    def __init__(self):
        super().__init__()

        self.angle = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)  # ~60 FPS

        self.setMinimumSize(420, 420)

    def animate(self):
        self.angle += 1

        if self.angle >= 360:
            self.angle = 0

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), Qt.transparent)

        cx = self.width() / 2
        cy = self.height() / 2

        # -------- OUTER RING --------

        painter.save()

        painter.translate(cx, cy)
        painter.rotate(self.angle)

        pen = QPen(QColor("#00D8FF"))
        pen.setWidth(4)

        painter.setPen(pen)

        painter.drawEllipse(-160, -160, 320, 320)

        for i in range(12):
            painter.drawLine(0, -145, 0, -160)
            painter.rotate(30)

        painter.restore()

        # -------- INNER RING --------

        painter.save()

        painter.translate(cx, cy)
        painter.rotate(-self.angle * 1.6)

        pen = QPen(QColor("#00FFFF"))
        pen.setWidth(3)

        painter.setPen(pen)

        painter.drawEllipse(-110, -110, 220, 220)

        for i in range(8):
            painter.drawLine(0, -98, 0, -110)
            painter.rotate(45)

        painter.restore()

        # -------- CENTER CORE --------

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#00D8FF"))

        painter.drawEllipse(int(cx - 40), int(cy - 40), 80, 80)

        # -------- GLOW --------

        painter.setBrush(QColor(0, 216, 255, 70))

        painter.drawEllipse(int(cx - 60), int(cy - 60), 120, 120)

        # -------- ORBITING NODE --------

        x = cx + math.cos(math.radians(self.angle * 2)) * 160
        y = cy + math.sin(math.radians(self.angle * 2)) * 160

        painter.setBrush(QColor("#7DF9FF"))
        painter.drawEllipse(int(x - 8), int(y - 8), 16, 16)