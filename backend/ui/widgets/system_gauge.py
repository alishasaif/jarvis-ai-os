from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import Qt


class SystemGauge(QWidget):

    def __init__(self, title):

        super().__init__()

        self.title = title
        self.value = 0

        self.setMinimumSize(
            140,
            140
        )


    def setValue(self, value):

        self.value = float(value)

        self.update()



    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )


        rect = self.rect()

        center = rect.center()


        radius = 45



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


        painter.drawEllipse(
            center,
            radius,
            radius
        )



        # Active orange ring

        pen = QPen(
            QColor("#FF9A1F")
        )

        pen.setWidth(
            10
        )

        pen.setCapStyle(
            Qt.PenCapStyle.RoundCap
        )


        painter.setPen(
            pen
        )


        painter.drawArc(
            center.x()-radius,
            center.y()-radius,
            radius*2,
            radius*2,
            90*16,
            -int(self.value * 3.6) * 16
        )



        # Percentage text

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



        # Label

        painter.setFont(
            QFont(
                "Arial",
                9
            )
        )


        painter.drawText(
            0,
            self.height()-10,
            self.width(),
            20,
            Qt.AlignmentFlag.AlignCenter,
            self.title
        )