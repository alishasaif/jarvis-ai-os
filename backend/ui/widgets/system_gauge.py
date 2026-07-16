from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen


class SystemGauge(QWidget):

    def __init__(self, title):

        super().__init__()

        self.title = title
        self.value = 0

        self.setMinimumSize(
            140,
            140
        )

        self.setMaximumHeight(
            150
        )


    def setValue(self, value):

        self.value = value
        self.update()



    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )


        size = min(
            self.width(),
            self.height()
        )


        rect_size = size - 20


        x = (
            self.width()
            -
            rect_size
        ) / 2


        y = (
            self.height()
            -
            rect_size
        ) / 2



        # Background ring

        pen = QPen(
            QColor("#263238")
        )

        pen.setWidth(
            10
        )

        painter.setPen(
            pen
        )


        painter.drawArc(
            int(x),
            int(y),
            int(rect_size),
            int(rect_size),
            0,
            360 * 16
        )



        # Value ring

        pen = QPen(
            QColor("#00E5FF")
        )

        pen.setWidth(
            10
        )

        painter.setPen(
            pen
        )


        angle = int(
            self.value * 3.6 * 16
        )


        painter.drawArc(
            int(x),
            int(y),
            int(rect_size),
            int(rect_size),
            90 * 16,
            -angle
        )



        # Text

        painter.setPen(
            QColor("#FFFFFF")
        )


        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            f"{self.value}%"
        )



        # Label

        painter.drawText(
            0,
            self.height()-5,
            self.title
        )