import platform
import socket
import time

import psutil


class SystemMonitor:

    boot_time = psutil.boot_time()

    @staticmethod
    def get_cpu():
        return float(
            psutil.cpu_percent(interval=None)
        )

    @staticmethod
    def get_ram():
        return float(
            psutil.virtual_memory().percent
        )

    @staticmethod
    def get_disk():
        return float(
            psutil.disk_usage("/").percent
        )

    @staticmethod
    def get_battery():

        battery = psutil.sensors_battery()

        if battery is None:
            return None

        return int(
            battery.percent
        )

    @staticmethod
    def get_network():

        net = psutil.net_io_counters()

        upload = round(
            net.bytes_sent / (1024 * 1024),
            2
        )

        download = round(
            net.bytes_recv / (1024 * 1024),
            2
        )

        return {
            "upload": upload,
            "download": download
        }

    @staticmethod
    def get_gpu():

        try:

            import GPUtil

            gpus = GPUtil.getGPUs()

            if gpus:
                return gpus[0].name

        except Exception:
            pass

        return "N/A"

    @staticmethod
    def get_device():
        return platform.node()

    @staticmethod
    def get_os():
        return platform.system() + " " + platform.release()

    @staticmethod
    def get_ip():

        try:
            hostname = socket.gethostname()
            return socket.gethostbyname(
                hostname
            )

        except Exception:
            return "Unknown"

    @staticmethod
    def get_uptime():

        uptime_seconds = (
            time.time() - SystemMonitor.boot_time
        )

        hours = int(
            uptime_seconds // 3600
        )

        minutes = int(
            (uptime_seconds % 3600) // 60
        )

        return f"{hours}h {minutes}m"

    @staticmethod
    def get_all():

        return {

            "cpu":
                SystemMonitor.get_cpu(),

            "ram":
                SystemMonitor.get_ram(),

            "disk":
                SystemMonitor.get_disk(),

            "battery":
                SystemMonitor.get_battery(),

            "network":
                SystemMonitor.get_network(),

            "gpu":
                SystemMonitor.get_gpu(),

            "device":
                SystemMonitor.get_device(),

            "os":
                SystemMonitor.get_os(),

            "ip":
                SystemMonitor.get_ip(),

            "uptime":
                SystemMonitor.get_uptime()

        }