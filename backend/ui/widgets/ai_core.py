from math import cos, sin, radians

from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget


class AICore(QWidget):

    def __init__(self):

        super().__init__()

        self.angle = 0
        self.state = "IDLE"

        self.colors = {
            "IDLE": QColor("#00E5FF"),
            "LISTENING": QColor("#00FFFF"),
            "THINKING": QColor("#FF9A1F"),
            "SPEAKING": QColor("#00FF66"),
            "EXECUTING": QColor("#00FF66"),
            "ERROR": QColor("#FF3030"),
        }

        self.speed = 2

        self.setMinimumSize(
            420,
            420
        )


        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(
            16
        )


    def animate(self):

        self.angle += self.speed

        if self.angle >= 360:
            self.angle = 0

        self.update()



    @Slot(object)
    def set_state(self, state):

        state = str(state)

        if state in self.colors:
            self.state = state


        if state == "THINKING":

            self.speed = 8

        elif state == "SPEAKING":

            self.speed = 5

        elif state == "EXECUTING":

            self.speed = 5

        elif state == "LISTENING":

            self.speed = 3

        else:

            self.speed = 2


        self.update()



    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )


        painter.fillRect(
            self.rect(),
            QColor("#070B14")
        )


        cx = self.width()/2
        cy = self.height()/2


        color = self.colors.get(
            self.state,
            QColor("#00E5FF")
        )


        pen = QPen(color)

        pen.setWidth(3)

        painter.setPen(pen)



        painter.drawEllipse(
            int(cx-140),
            int(cy-140),
            280,
            280
        )


        painter.save()

        painter.translate(
            cx,
            cy
        )

        painter.rotate(
            self.angle
        )


        pen.setWidth(2)

        painter.setPen(
            pen
        )


        painter.drawEllipse(
            -100,
            -100,
            200,
            200
        )


        painter.restore()



        painter.save()

        painter.translate(
            cx,
            cy
        )

        painter.rotate(
            -self.angle*1.5
        )


        painter.drawEllipse(
            -70,
            -70,
            140,
            140
        )


        painter.restore()



        painter.setBrush(
            color
        )

        painter.setPen(
            Qt.NoPen
        )


        painter.drawEllipse(
            int(cx-25),
            int(cy-25),
            50,
            50
        )


        x = cx + cos(radians(self.angle))*120
        y = cy + sin(radians(self.angle))*120


        painter.drawEllipse(
            int(x-6),
            int(y-6),
            12,
            12
        )


        painter.setPen(
            QColor("#8FD9FF")
        )


        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            self.state
        )