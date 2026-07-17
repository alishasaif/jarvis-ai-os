"""
System Service
Provides live system data to the UI
and publishes updates through the
global event bus.
"""

from backend.system.system_monitor import SystemMonitor
from backend.core.jarvis_events import jarvis_events


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

    @staticmethod
    def publish_stats():

        stats = SystemService.get_stats()

        jarvis_events.cpu_changed.emit(
            stats["cpu"]
        )

        jarvis_events.ram_changed.emit(
            stats["ram"]
        )

        jarvis_events.disk_changed.emit(
            stats["disk"]
        )

        jarvis_events.network_changed.emit(
            stats["network"]
        )

        jarvis_events.battery_changed.emit(
            stats["battery"]
        )

        jarvis_events.system_updated.emit(
            stats
        )

        return stats