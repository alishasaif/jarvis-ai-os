from PySide6.QtCore import QTimer, QPointF, Qt
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget
import random


class Particle:

    def __init__(self, width, height):

        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

        self.size = random.randint(2, 5)

        self.dx = random.uniform(-0.4, 0.4)
        self.dy = random.uniform(-0.4, 0.4)

        self.alpha = random.randint(60, 180)


class ParticleBackground(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self.particles = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def resizeEvent(self, event):

        if not self.particles:

            for _ in range(70):
                self.particles.append(
                    Particle(self.width(), self.height())
                )

        super().resizeEvent(event)

    def animate(self):

        for p in self.particles:

            p.x += p.dx
            p.y += p.dy

            if p.x < 0:
                p.x = self.width()

            if p.x > self.width():
                p.x = 0

            if p.y < 0:
                p.y = self.height()

            if p.y > self.height():
                p.y = 0

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for p in self.particles:

            color = QColor(0, 216, 255, p.alpha)

            painter.setBrush(color)
            painter.setPen(color)

            painter.drawEllipse(
                QPointF(p.x, p.y),
                p.size,
                p.size
            )