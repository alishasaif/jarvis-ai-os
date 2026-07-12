from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame,
)


class StatusItem(QFrame):
    """
    Small status indicator used inside Mission Control.
    """

    def __init__(self, title, value="OFFLINE"):
        super().__init__()

        self.setObjectName("MissionItem")

        layout = QVBoxLayout(self)

        self.title = QLabel(title)
        self.title.setObjectName("MissionTitle")

        self.value = QLabel(value)
        self.value.setObjectName("MissionValue")

        layout.addWidget(self.title)
        layout.addWidget(self.value)

    def set_status(self, text):
        self.value.setText(text)


class MissionControl(QWidget):
    """
    Mission Control Panel
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("MissionControl")

        layout = QVBoxLayout(self)

        title = QLabel("MISSION CONTROL")
        title.setObjectName("MissionHeader")

        layout.addWidget(title)

        self.ai = StatusItem("AI Engine")
        self.voice = StatusItem("Voice Engine")
        self.memory = StatusItem("Memory")
        self.internet = StatusItem("Internet")
        self.ollama = StatusItem("Ollama")
        self.openai = StatusItem("OpenAI")
        self.android = StatusItem("Android")
        self.automation = StatusItem("Automation")

        layout.addWidget(self.ai)
        layout.addWidget(self.voice)
        layout.addWidget(self.memory)
        layout.addWidget(self.internet)
        layout.addWidget(self.ollama)
        layout.addWidget(self.openai)
        layout.addWidget(self.android)
        layout.addWidget(self.automation)

        layout.addStretch()

    def update_status(self, component, status):
        """
        Update a component's status.
        """

        mapping = {
            "ai": self.ai,
            "voice": self.voice,
            "memory": self.memory,
            "internet": self.internet,
            "ollama": self.ollama,
            "openai": self.openai,
            "android": self.android,
            "automation": self.automation,
        }

        if component in mapping:
            mapping[component].set_status(status)