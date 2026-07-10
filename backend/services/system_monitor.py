import psutil
import time


class SystemMonitor:
    def __init__(self):
        self.start_time = time.time()

    def get_cpu(self):
        return psutil.cpu_percent(interval=None)

    def get_ram(self):
        return psutil.virtual_memory().percent

    def get_disk(self):
        return psutil.disk_usage("/").percent

    def get_network_status(self):
        stats = psutil.net_if_stats()

        for interface in stats.values():
            if interface.isup:
                return "🟢 ONLINE"

        return "🔴 OFFLINE"

    def get_uptime(self):
        seconds = int(time.time() - self.start_time)

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        return f"{hours:02}:{minutes:02}:{secs:02}"