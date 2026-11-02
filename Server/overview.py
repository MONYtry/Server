
###################
# SERVER OVERVIEW #
# Made by MONY    #
# Running & tested on UBUNTU #
###################

import psutil
import time
import os

RefreshTime = 5
RefreshCount = 0

RED = "\033[91m"
GREEN = "\033[92m"
WHITE = "\033[0m"  


def getRAM():
    RAM = psutil.virtual_memory()

    RAM_TOTAL = RAM.total / (1024**3)
    RAM_USED = RAM.used / (1024**3)
    RAM_FREE = RAM.available / (1024**3)
    
    return RAM_FREE, RAM_TOTAL, RAM_USED


def getDisk():
    DISK = psutil.disk_usage("/")

    DISK_USAGE = DISK.used / (1024**3)
    DISK_FREE = DISK.free / (1024**3)
    DISK_TOTAL = DISK.total / (1024**3)
    DISK_PERCENT = DISK.percent
    return DISK_FREE, DISK_PERCENT, DISK_TOTAL, DISK_USAGE

def getUptime():
    UPTIME = time.time() - psutil.boot_time()

    HOURS = int(UPTIME // 3600)
    MINUTES = int((UPTIME % 3600) // 60)
    SECONDS = int(UPTIME % 60)

    return SECONDS, MINUTES, HOURS

def getNetwork():
    NET = psutil.net_io_counters()
    UPLOAD = NET.bytes_sent / (1024**3)
    DOWNLOAD = NET.bytes_recv / (1024**3)

    return UPLOAD, DOWNLOAD

while True:

    os.system("clear")
    
    UPLOAD, DOWNLOAD = getNetwork()

    SECONDS, MINUTES, HOURS = getUptime()

    # 1024**3 von Bytes auf GB
    RAM_FREE, RAM_TOTAL, RAM_USED = getRAM()
    

    CPU_USAGE = psutil.cpu_percent()

    DISK_FREE,DISK_PERCENT, DISK_TOTAL, DISK_USAGE = getDisk()


    # Using :. for formating Numbers
    print("#### RAM-Infomation ###\n")
    print(f"Gesamter Ram: {RAM_TOTAL:.1f} GB")
    print(f"Genutzer Ram: {RAM_USED:.1f} GB")
    print(f"Freier Ram: {RAM_FREE:.1f} GB \n")

    print("#### CPU-Infomation ###\n")
    print(f"CPU Usage: {CPU_USAGE}% \n")

    print("#### DISC-Infomation ###\n")
    print(f"Disk-Usage: {DISK_USAGE:.1f}")
    print(f"Disk-Free: {DISK_FREE:.1f}")
    print(f"Disk-total: {DISK_TOTAL:.1f}")
    print(f"Disk-Percent: {DISK_PERCENT:.1f}%\n")

    print("#### NETWORK-Infomation ###\n")
    print(f"Upload: {UPLOAD:.2f} MB/s")
    print(f"Download: {DOWNLOAD:.2f} MB/s")
    

    print("#### Infomation ###\n")
    print(f"Server Uptime: {HOURS}h {MINUTES}m {SECONDS}s")
    print(f"Nächste aktualiserung in {RefreshTime}...")
    print(f"Aktuelle aktualiserung [#{RefreshCount}]")
    print("Press [CTRL + C] to quit...")

    time.sleep(RefreshTime)
    
    RefreshCount = +1
    
