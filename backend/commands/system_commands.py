"""
J.A.R.V.I.S System Commands
"""

from backend.services.system_service import SystemService


class SystemCommands:

    def cpu(self):
        stats = SystemService.get_stats()
        return f"CPU Usage: {stats['cpu']}%"

    def ram(self):
        stats = SystemService.get_stats()
        return f"RAM Usage: {stats['ram']}%"

    def disk(self):
        stats = SystemService.get_stats()
        return f"Disk Usage: {stats['disk']}%"