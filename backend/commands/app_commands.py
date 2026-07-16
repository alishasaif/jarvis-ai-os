"""
J.A.R.V.I.S Application Commands
"""

import subprocess
import shutil


class AppCommands:

    def open_notepad(self):

        subprocess.Popen("notepad.exe")

        return "Opening Notepad."

    def open_calculator(self):

        subprocess.Popen("calc.exe")

        return "Opening Calculator."

    def open_chrome(self):

        chrome = shutil.which("chrome")

        if chrome:
            subprocess.Popen([chrome])
            return "Opening Google Chrome."

        paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]

        for path in paths:

            try:
                subprocess.Popen([path])
                return "Opening Google Chrome."

            except Exception:
                pass

        return "Google Chrome is not installed."