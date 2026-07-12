"""
J.A.R.V.I.S AI OS Theme
Version: 0.2
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    BACKGROUND = "#070B14"
    PANEL = "#101826"
    PANEL_ALT = "#151F30"

    PRIMARY = "#00E5FF"
    PRIMARY_DARK = "#0099CC"

    SUCCESS = "#00FF88"
    WARNING = "#FFC107"
    ERROR = "#FF5252"

    TEXT = "#FFFFFF"
    TEXT_SECONDARY = "#8FA9C7"

    BORDER = "#1E3A5F"


class Theme:

    @staticmethod
    def stylesheet():

        return f"""

        QWidget {{
            background: {Colors.BACKGROUND};
            color: {Colors.TEXT};
            font-family: "Segoe UI";
            font-size: 10pt;
        }}

        QMainWindow {{
            background: {Colors.BACKGROUND};
        }}

        QFrame {{
            background: {Colors.PANEL};
            border: 1px solid {Colors.BORDER};
            border-radius: 12px;
        }}

        QLabel {{
            background: transparent;
        }}

        QPushButton {{

            background: {Colors.PANEL_ALT};

            border: 1px solid {Colors.BORDER};

            border-radius: 10px;

            padding: 8px;

            color: {Colors.TEXT};

        }}

        QPushButton:hover {{

            background: {Colors.PRIMARY};

            color: black;

        }}

        QListWidget {{

            background: {Colors.PANEL};

            border: none;

            outline: none;

        }}

        QListWidget::item {{

            padding: 12px;

        }}

        QListWidget::item:selected {{

            background: {Colors.PRIMARY};

            color: black;

            border-radius: 8px;

        }}

        QTextEdit {{

            background: {Colors.PANEL};

            border: 1px solid {Colors.BORDER};

            border-radius: 10px;

        }}

        """