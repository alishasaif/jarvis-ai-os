"""
System Monitor
Collects live system information for J.A.R.V.I.S.
"""

import platform
import socket
import time

import psutil

try:
    import GPUtil
except ImportError:
    GPUtil = None


class SystemMonitor:
    @staticmethod
    def get_cpu():
        return psutil.cpu_percent(interval=0.1)

    @staticmethod
    def get_ram():
        return psutil.virtual_memory().percent

    @staticmethod
    def get_disk():
        return psutil.disk_usage("/").percent

    @staticmethod
    def get_battery():
        battery = psutil.sensors_battery()

        if battery is None:
            return "N/A"

        return f"{battery.percent:.0f}%"

    @staticmethod
    def get_network():
        net = psutil.net_io_counters()

        up = net.bytes_sent / (1024 * 1024)
        down = net.bytes_recv / (1024 * 1024)

        return f"↑ {up:.1f} MB | ↓ {down:.1f} MB"

    @staticmethod
    def get_gpu():
        if GPUtil is None:
            return "N/A"

        try:
            gpus = GPUtil.getGPUs()

            if not gpus:
                return "N/A"

            return f"{gpus[0].load * 100:.0f}%"

        except Exception:
            return "N/A"

    @staticmethod
    def get_device():
        return socket.gethostname()

    @staticmethod
    def get_os():
        return f"{platform.system()} {platform.release()}"

    @staticmethod
    def get_uptime():
        seconds = int(time.time() - psutil.boot_time())

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        return f"{hours}h {minutes}m"