from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QColor, QPen
import math


class ArcReactor(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(420, 420)

        self.angle1 = 0
        self.angle2 = 0
        self.angle3 = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)      # ~60 FPS

    def animate(self):

        self.angle1 += 1
        self.angle2 -= 2
        self.angle3 += 3

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width()/2, self.height()/2)

        self.draw_ring(painter, 150, self.angle1, 4)
        self.draw_ring(painter, 115, self.angle2, 3)
        self.draw_ring(painter, 80, self.angle3, 2)

        # Core
        painter.setBrush(QColor(0,216,255))
        painter.setPen(QPen(QColor(0,216,255),2))
        painter.drawEllipse(-25,-25,50,50)

        # Outer Nodes
        for i in range(8):

            angle = math.radians(i*45 + self.angle1)

            x = math.cos(angle)*150
            y = math.sin(angle)*150

            painter.setBrush(QColor(0,216,255))
            painter.drawEllipse(int(x)-5, int(y)-5,10,10)

    def draw_ring(self,painter,radius,rotation,width):

        painter.save()

        painter.rotate(rotation)

        pen = QPen(QColor(0,216,255))
        pen.setWidth(width)

        painter.setPen(pen)

        for i in range(0,360,30):

            painter.drawArc(
                -radius,
                -radius,
                radius*2,
                radius*2,
                i*16,
                18*16
            )

        painter.restore()