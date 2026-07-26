from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter, QColor, QPen, QFont


class SystemGauge(QWidget):

    def __init__(self, title):

        super().__init__()

        self.title = str(title)
        self.value = 0.0

        self.setMinimumSize(170, 170)
        self.setMaximumSize(170, 170)

    @Slot(float)
    def setValue(self, value):

        try:
            self.value = max(
                0.0,
                min(
                    100.0,
                    float(value)
                )
            )

        except Exception:

            self.value = 0.0

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()

        size = min(w, h) - 20

        rect_x = (w - size) / 2
        rect_y = 8

        pen = QPen(QColor("#25303A"))
        pen.setWidth(12)
        painter.setPen(pen)

        painter.drawEllipse(
            int(rect_x),
            int(rect_y),
            int(size),
            int(size)
        )

        pen = QPen(QColor("#15E3FF"))
        pen.setWidth(12)
        pen.setCapStyle(Qt.RoundCap)

        painter.setPen(pen)

        span = int(-360 * 16 * self.value / 100)

        painter.drawArc(
            int(rect_x),
            int(rect_y),
            int(size),
            int(size),
            90 * 16,
            span
        )

        painter.setPen(QColor("#FFFFFF"))

        font = QFont("Segoe UI", 12)
        font.setBold(True)

        painter.setFont(font)

        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            f"{self.value:.1f}%"
        )

        painter.setPen(QColor("#FFFFFF"))

        font = QFont("Segoe UI", 10)

        painter.setFont(font)

        painter.drawText(
            0,
            h - 18,
            w,
            20,
            Qt.AlignCenter,
            str(self.title)
        )