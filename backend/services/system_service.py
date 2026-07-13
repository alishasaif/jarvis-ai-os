"""
System Service
Provides live system data to the UI.
"""

from backend.system.system_monitor import SystemMonitor


class SystemService:

    @staticmethod
    def get_stats():
        return {
            "cpu": SystemMonitor.get_cpu(),
            "ram": SystemMonitor.get_ram(),
            "disk": SystemMonitor.get_disk(),
            "battery": SystemMonitor.get_battery(),
            "network": SystemMonitor.get_network(),
            "gpu": SystemMonitor.get_gpu(),
            "device": SystemMonitor.get_device(),
            "os": SystemMonitor.get_os(),
            "uptime": SystemMonitor.get_uptime(),
        }