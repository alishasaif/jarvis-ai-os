from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QColor, QPen
import math


class ArcReactor(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumSize(420, 420)

        self.angle1 = 0
        self.angle2 = 0
        self.angle3 = 0

        self.pulse = 0
        self.growing = True


        # Animation timer
        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(16)



    def animate(self):

        self.angle1 += 1
        self.angle2 -= 2
        self.angle3 += 3


        if self.growing:

            self.pulse += 0.5

            if self.pulse >= 15:
                self.growing = False


        else:

            self.pulse -= 0.5

            if self.pulse <= 0:
                self.growing = True


        self.update()



    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )


        painter.translate(
            self.width()/2,
            self.height()/2
        )



        color = QColor(
            0,
            216,
            255
        )



        # Outer energy glow

        for radius in range(170,210,8):

            painter.setPen(
                QPen(
                    QColor(
                        0,
                        216,
                        255,
                        30
                    ),
                    2
                )
            )


            painter.drawEllipse(
                -radius,
                -radius,
                radius*2,
                radius*2
            )



        # Rotating rings

        self.draw_ring(
            painter,
            150,
            self.angle1,
            4,
            color
        )


        self.draw_ring(
            painter,
            110,
            self.angle2,
            3,
            color
        )


        self.draw_ring(
            painter,
            75,
            self.angle3,
            2,
            color
        )



        # Orbit nodes

        painter.setBrush(color)

        painter.setPen(
            Qt.NoPen
        )


        for i in range(12):

            angle = math.radians(
                i*30+self.angle1
            )


            x = math.cos(angle)*150
            y = math.sin(angle)*150


            painter.drawEllipse(
                int(x)-5,
                int(y)-5,
                10,
                10
            )



        # Core glow

        glow = int(
            50+self.pulse
        )


        painter.setBrush(
            QColor(
                0,
                216,
                255,
                50
            )
        )


        painter.drawEllipse(
            -glow,
            -glow,
            glow*2,
            glow*2
        )



        # Main reactor body

        painter.setPen(
            QPen(
                color,
                3
            )
        )


        painter.setBrush(
            QColor(
                5,
                25,
                40
            )
        )


        painter.drawEllipse(
            -35,
            -35,
            70,
            70
        )



        # Inner energy

        core = int(
            25+self.pulse/3
        )


        painter.setPen(
            Qt.NoPen
        )


        painter.setBrush(
            color
        )


        painter.drawEllipse(
            -core,
            -core,
            core*2,
            core*2
        )



        # White center

        painter.setBrush(
            QColor(
                255,
                255,
                255
            )
        )


        painter.drawEllipse(
            -8,
            -8,
            16,
            16
        )



    def draw_ring(
            self,
            painter,
            radius,
            rotation,
            width,
            color):


        painter.save()

        painter.rotate(
            rotation
        )


        painter.setPen(
            QPen(
                color,
                width
            )
        )


        painter.setBrush(
            Qt.NoBrush
        )


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