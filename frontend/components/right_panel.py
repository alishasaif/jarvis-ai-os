from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)


class RightPanel(QWidget):

    def __init__(self):

        super().__init__()


        layout = QVBoxLayout()


        title = QLabel(
            "JARVIS CORE"
        )


        title.setStyleSheet("""
            QLabel{
                color:#00d8ff;
                font-size:18px;
                font-weight:bold;
            }
        """)


        layout.addWidget(title)



        self.ai_status = QLabel(
            "AI STATUS : ONLINE"
        )

        self.memory = QLabel(
            "MEMORY : READY"
        )

        self.voice = QLabel(
            "VOICE : STANDBY"
        )

        self.model = QLabel(
            "MODEL : NOT CONNECTED"
        )


        items = [
            self.ai_status,
            self.memory,
            self.voice,
            self.model
        ]


        for item in items:

            item.setStyleSheet("""
                QLabel{
                    color:#9eeaff;
                    font-size:14px;
                    padding:8px;
                    border:1px solid #003344;
                    border-radius:6px;
                }
            """)


            layout.addWidget(item)



        layout.addStretch()


        self.setLayout(
            layout
        )


        self.setFixedWidth(
            250
        )