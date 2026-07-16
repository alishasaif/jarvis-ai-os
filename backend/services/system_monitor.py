import psutil
import platform
import socket
import time


class SystemMonitor:

    boot_time = psutil.boot_time()


    @staticmethod
    def get_cpu():
        return psutil.cpu_percent(interval=0.5)


    @staticmethod
    def get_ram():
        return psutil.virtual_memory().percent


    @staticmethod
    def get_disk():
        return psutil.disk_usage('/').percent


    @staticmethod
    def get_battery():

        battery = psutil.sensors_battery()

        if battery:
            return battery.percent

        return "N/A"


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
    def get_device():

        return platform.node()


    @staticmethod
    def get_os():

        return platform.system() + " " + platform.release()


    @staticmethod
    def get_ip():

        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)

            return ip

        except:

            return "Unknown"


    @staticmethod
    def get_uptime():

        uptime_seconds = time.time() - SystemMonitor.boot_time

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

            "device":
                SystemMonitor.get_device(),

            "os":
                SystemMonitor.get_os(),

            "ip":
                SystemMonitor.get_ip(),

            "uptime":
                SystemMonitor.get_uptime()

        }