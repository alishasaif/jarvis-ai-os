from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QFont,
)


class AICore(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(420, 420)

        self.radius = 90
        self.growing = True

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)   # ~60 FPS

    def animate(self):

        if self.growing:
            self.radius += 0.4
            if self.radius >= 100:
                self.growing = False
        else:
            self.radius -= 0.4
            if self.radius <= 90:
                self.growing = True

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), QColor("#05070B"))

        center = self.rect().center()

        glow = QColor(0, 216, 255, 40)

        for i in range(10):
            pen = QPen(glow)
            pen.setWidth(20 - i * 2)
            painter.setPen(pen)

            painter.drawEllipse(
                center,
                int(self.radius + i * 3),
                int(self.radius + i * 3),
            )

        pen = QPen(QColor("#00D8FF"))
        pen.setWidth(4)

        painter.setPen(pen)

        painter.drawEllipse(
            center,
            int(self.radius),
            int(self.radius),
        )

        font = QFont("Segoe UI", 20)
        font.setBold(True)

        painter.setFont(font)
        painter.setPen(QColor("#00D8FF"))

        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            "JARVIS"
        )

        font2 = QFont("Segoe UI", 10)

        painter.setFont(font2)

        painter.drawText(
            0,
            center.y() + 40,
            self.width(),
            30,
            Qt.AlignCenter,
            "AI CORE ONLINE"
        )