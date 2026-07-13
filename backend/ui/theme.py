"""
J.A.R.V.I.S AI OS Theme
Version: 3.0
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    BACKGROUND = "#060A12"
    PANEL = "#101826"
    PANEL_ALT = "#141F31"

    PRIMARY = "#00E5FF"
    PRIMARY_HOVER = "#35F2FF"
    PRIMARY_DARK = "#0088CC"

    SUCCESS = "#00FF88"
    WARNING = "#FFC107"
    ERROR = "#FF5252"

    TEXT = "#FFFFFF"
    TEXT_SECONDARY = "#8FA9C7"

    BORDER = "#1E3A5F"
    BORDER_GLOW = "#00E5FF"


class Theme:

    @staticmethod
    def stylesheet():

        return """
QWidget {{
    background: {BACKGROUND};
    color: {TEXT};
    font-family: "Segoe UI";
    font-size: 10pt;
}}

QMainWindow {{
    background: {BACKGROUND};
}}

QFrame {{
    background: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 14px;
}}

QFrame:hover {{
    border: 1px solid {BORDER_GLOW};
}}

QLabel {{
    background: transparent;
    color: {TEXT};
}}

#SystemCard {{
    background: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 16px;
}}

#SystemCard:hover {{
    border: 2px solid {PRIMARY};
}}

#SystemCardTitle {{
    color: {TEXT_SECONDARY};
    font-size: 11pt;
    font-weight: bold;
}}

#SystemCardValue {{
    color: {PRIMARY};
    font-size: 18pt;
    font-weight: bold;
}}

QPushButton {{
    background: {PANEL_ALT};
    border: 1px solid {BORDER};
    border-radius: 10px;
    padding: 8px;
}}

QPushButton:hover {{
    background: {PRIMARY};
    color: black;
}}

QLineEdit {{
    background: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 10px;
    padding: 8px;
    color: white;
}}

QLineEdit:focus {{
    border: 1px solid {PRIMARY};
}}

QTextEdit {{
    background: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 12px;
    padding: 10px;
}}

QListWidget {{
    background: {PANEL};
    border: none;
    outline: none;
}}

QListWidget::item {{
    padding: 14px;
    margin: 4px;
    border-radius: 10px;
}}

QListWidget::item:selected {{
    background: {PRIMARY};
    color: black;
    font-weight: bold;
}}

QListWidget::item:hover {{
    background: #17304C;
}}

QScrollBar:vertical {{
    background: {PANEL};
    width: 8px;
    border: none;
}}

QScrollBar::handle:vertical {{
    background: {PRIMARY};
    border-radius: 4px;
}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height: 0px;
}}
""".format(
            BACKGROUND=Colors.BACKGROUND,
            PANEL=Colors.PANEL,
            PANEL_ALT=Colors.PANEL_ALT,
            PRIMARY=Colors.PRIMARY,
            BORDER=Colors.BORDER,
            BORDER_GLOW=Colors.BORDER_GLOW,
            TEXT=Colors.TEXT,
            TEXT_SECONDARY=Colors.TEXT_SECONDARY,
        )