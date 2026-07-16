"""
J.A.R.V.I.S Theme
"""

# ==========================
# COLORS
# ==========================

BACKGROUND = "#050505"
PANEL = "#101010"
PANEL_DARK = "#0A0A0A"

PRIMARY = "#FF9A1F"
PRIMARY_LIGHT = "#FFB347"
PRIMARY_DARK = "#D97706"

BORDER = "#7A4A11"

TEXT = "#FFD79A"
TEXT_SECONDARY = "#B88A4A"

SUCCESS = "#00FF88"
WARNING = "#FFCC00"
ERROR = "#FF5555"

GLOW_RADIUS = 20


class Theme:
    """
    Compatibility wrapper for the UI.
    Existing widgets can call Theme.stylesheet().
    New widgets can import the constants directly.
    """

    @staticmethod
    def stylesheet():
        return f"""
        QWidget {{
            background-color: {BACKGROUND};
            color: {TEXT};
            font-family: Segoe UI;
            font-size: 10pt;
        }}

        QPushButton {{
            background-color: {PRIMARY};
            color: black;
            border-radius: 8px;
            padding: 6px 12px;
            font-weight: bold;
        }}

        QPushButton:hover {{
            background-color: {PRIMARY_LIGHT};
        }}

        QLineEdit,
        QTextEdit {{
            background-color: {PANEL};
            color: {TEXT};
            border: 1px solid {BORDER};
            border-radius: 8px;
            padding: 6px;
        }}
        """
