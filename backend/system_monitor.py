import psutil
import platform
import socket


class SystemMonitor:

    @staticmethod
    def get_cpu():
        return psutil.cpu_percent(interval=1)


    @staticmethod
    def get_ram():
        memory = psutil.virtual_memory()
        return memory.percent


    @staticmethod
    def get_disk():
        disk = psutil.disk_usage('/')
        return disk.percent


    @staticmethod
    def get_device():
        return platform.node()


    @staticmethod
    def get_os():
        return platform.system()


    @staticmethod
    def get_network():
        try:
            return socket.gethostbyname(socket.gethostname())
        except:
            return "Offline"