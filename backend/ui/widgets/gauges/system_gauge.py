from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import Qt


class SystemGauge(QWidget):

    def __init__(self, title):

        super().__init__()

        self.title = title
        self.value = 0

        self.setMinimumSize(
            130,
            130
        )


    def setValue(self, value):

        self.value = value
        self.update()


    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )


        rect = self.rect()

        center = rect.center()

        radius = 45


        # outer circle

        pen = QPen(
            QColor("#1b2638")
        )

        pen.setWidth(10)

        painter.setPen(
            pen
        )

        painter.drawEllipse(
            center,
            radius,
            radius
        )


        # progress arc

        pen = QPen(
            QColor("#FF9A1F")
        )

        pen.setWidth(10)

        painter.setPen(
            pen
        )


        painter.drawArc(
            center.x()-radius,
            center.y()-radius,
            radius*2,
            radius*2,
            90*16,
            -int(self.value*3.6)*16
        )


        # value text

        painter.setPen(
            QColor("#FFFFFF")
        )

        painter.setFont(
            QFont(
                "Arial",
                14,
                QFont.Weight.Bold
            )
        )


        painter.drawText(
            rect,
            Qt.AlignmentFlag.AlignCenter,
            f"{int(self.value)}%"
        )


        # title

        painter.setFont(
            QFont(
                "Arial",
                9
            )
        )

        painter.drawText(
            0,
            120,
            self.width(),
            20,
            Qt.AlignmentFlag.AlignCenter,
            self.title
        )