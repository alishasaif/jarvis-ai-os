from __future__ import annotations

import math

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget


class AICoreWidget(QWidget):
    """
    Animated AI Core Widget
    J.A.R.V.I.S AI OS
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(320, 320)

        # Animation values
        self.outer_rotation = 0.0
        self.inner_rotation = 0.0
        self.pulse = 0.0

        # 60 FPS animation timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):
        self.outer_rotation += 0.8
        self.inner_rotation -= 1.2
        self.pulse += 0.08

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), Qt.transparent)

        cx = self.width() / 2
        cy = self.height() / 2

        radius = min(self.width(), self.height()) / 3

        self.draw_outer_ring(painter, cx, cy, radius)
        self.draw_inner_ring(painter, cx, cy, radius * 0.72)
        self.draw_core(painter, cx, cy)

    def draw_outer_ring(self, painter, cx, cy, radius):

        painter.save()

        painter.translate(cx, cy)
        painter.rotate(self.outer_rotation)

        pen = QPen(QColor("#00E5FF"))
        pen.setWidth(3)

        painter.setPen(pen)

        painter.drawEllipse(
            int(-radius),
            int(-radius),
            int(radius * 2),
            int(radius * 2),
        )

        for angle in range(0, 360, 30):

            rad = math.radians(angle)

            x1 = math.cos(rad) * radius
            y1 = math.sin(rad) * radius

            x2 = math.cos(rad) * (radius + 12)
            y2 = math.sin(rad) * (radius + 12)

            painter.drawLine(
                int(x1),
                int(y1),
                int(x2),
                int(y2),
            )

        painter.restore()

    def draw_inner_ring(self, painter, cx, cy, radius):

        painter.save()

        painter.translate(cx, cy)
        painter.rotate(self.inner_rotation)

        pen = QPen(QColor("#66F7FF"))
        pen.setWidth(2)

        painter.setPen(pen)

        painter.drawEllipse(
            int(-radius),
            int(-radius),
            int(radius * 2),
            int(radius * 2),
        )

        painter.restore()

    def draw_core(self, painter, cx, cy):

        pulse = 18 + math.sin(self.pulse) * 5

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#00E5FF"))

        painter.drawEllipse(
            int(cx - pulse),
            int(cy - pulse),
            int(pulse * 2),
            int(pulse * 2),
        )