import psutil
import time
import sys
sys.path.append(".")

from helper import RED,GREEN,WHITE
from config import (Medium_RAM_Usage,
                     High_RAM_Usage,
                     Small_RAM_Usage,
                     Critical_RAM_Usage,
                     High_CPU_Usage,Critical_CPU_Usage,Small_CPU_Usage,Medium_CPU_Usage)

print(f"{'PID':<8} {'Prozessname':<20} {'RAM-Usage':<10} {'CPU-Usage':<10} {'Time':<10}" )
print("-" * 31)

processes = []

def createReport():
    global processes

    # Geht durch alle Prozesse
    # Fügt sie dem Array hinzu
    for p in psutil.process_iter(["pid", "name"]):
        processes.append(p)
        
    # Sortiert den Array nach Memory-Usage
    # Umgedreht = Von höchste zu niedrigste
    processes = sorted(processes, key=lambda p: p.memory_info().rss / (1024**2), reverse=True)


def sendReport():
    global processes    
    createReport()

    # Unsere Hauptfunktion 
    for p in processes:
        try:
            CPU_USAGE = getCpuUsage(p)
            RUNNING_TIME, RUNNING_UNIT = getUptime(p)
            
            RAM_USAGE, einheit = getRamUsage(p)
            
            print(f"{p.info['pid']:<8} | {p.info['name']:<25} | {RAM_USAGE:<10.2f} {einheit} | {CPU_USAGE:<10} | {RUNNING_TIME:<10.1f} {RUNNING_UNIT}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        
def getCpuUsage(p):
    CPU_USAGE = round(p.cpu_percent(interval=0.5), 2)
    CPU_USAGE_TEXT = str(CPU_USAGE) + "%"

    if CPU_USAGE >= High_CPU_Usage:
        CPU_USAGE_TEXT = RED + CPU_USAGE_TEXT + WHITE
    elif CPU_USAGE >= Medium_CPU_Usage:
        CPU_USAGE_TEXT = WHITE + CPU_USAGE_TEXT + WHITE
    elif CPU_USAGE <= Small_CPU_Usage:
        CPU_USAGE_TEXT = GREEN + CPU_USAGE_TEXT + WHITE
    return CPU_USAGE_TEXT

def getRamUsage(p):
    einheit = "MB"

    RAM_USAGE = p.memory_info().rss / (1024**2)
    RAM_USAGE_IN_GB = RAM_USAGE / 1000
    
    VALUE_TO_RETURN = RAM_USAGE

    if RAM_USAGE >= 1000:
        einheit = "GB"
        VALUE_TO_RETURN = RAM_USAGE_IN_GB
    
    if RAM_USAGE >= High_RAM_Usage:
        einheit = RED + einheit + WHITE
    
    elif RAM_USAGE >= Medium_RAM_Usage:
        einheit = WHITE + einheit + WHITE
    
    elif RAM_USAGE <= Small_RAM_Usage:
        einheit = GREEN + einheit + WHITE
    
    return VALUE_TO_RETURN, einheit



def getUptime(p):
    RUNNING_SECONDS = time.time() - p.create_time() 
    RUNNING_MINUTES = RUNNING_SECONDS / 60
    RUNNING_HOURS = RUNNING_MINUTES / 60
    RUNNING_UNIT = "sec"

    if RUNNING_SECONDS < 60:
        RUNNING_TIME = RUNNING_SECONDS
        RUNNING_UNIT = "sec"
    
    elif RUNNING_MINUTES < 60:
        RUNNING_TIME = RUNNING_MINUTES
        RUNNING_UNIT = "min"
    
    else:
        RUNNING_TIME = RUNNING_HOURS
        RUNNING_UNIT = "hrs"
    return RUNNING_TIME, RUNNING_UNIT



sendReport()