from math import cos, sin, radians

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget


class AICore(QWidget):
    """
    Animated AI Core
    """

    def __init__(self):
        super().__init__()

        self.angle = 0
        self.state = "IDLE"

        self.setMinimumSize(420, 420)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)  # ~60 FPS

    def animate(self):
        self.angle += 2

        if self.angle >= 360:
            self.angle = 0

        self.update()

    def set_state(self, state):
        self.state = state
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), QColor("#070B14"))

        cx = self.width() / 2
        cy = self.height() / 2

        # Outer Ring
        pen = QPen(QColor("#00E5FF"))
        pen.setWidth(3)
        painter.setPen(pen)

        painter.drawEllipse(
            int(cx - 140),
            int(cy - 140),
            280,
            280,
        )

        # Middle Ring
        painter.save()
        painter.translate(cx, cy)
        painter.rotate(self.angle)

        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawEllipse(-100, -100, 200, 200)

        painter.restore()

        # Inner Ring
        painter.save()
        painter.translate(cx, cy)
        painter.rotate(-self.angle * 1.5)

        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawEllipse(-70, -70, 140, 140)

        painter.restore()

        # Core
        painter.setBrush(QColor("#00E5FF"))
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(
            int(cx - 25),
            int(cy - 25),
            50,
            50,
        )

        # Orbiting Particle
        painter.setBrush(QColor("#00FFFF"))

        x = cx + cos(radians(self.angle)) * 120
        y = cy + sin(radians(self.angle)) * 120

        painter.drawEllipse(
            int(x - 6),
            int(y - 6),
            12,
            12,
        )

        # State Text
        painter.setPen(QColor("#8FD9FF"))
        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            self.state,
        )