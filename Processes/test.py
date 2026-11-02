
import psutil
import time

print(f"{'PID':<8} {'Prozessname':<20}")
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
        einheit = "MB"
        einheit_time = 0
        einheit_time_display = "sec"
        
        CPU_USAGE = p.cpu_percent()
        RAM_USAGE = p.memory_info().rss / (1024**2)

        
        RUNNING_TIME, RUNNING_UNIT = getUptime(p)
        if RAM_USAGE >= 1000:
            einheit = "GB"

        print(f"{p.info['pid']:<8} | {p.info['name']:<25} | {RAM_USAGE:<10.2f} {einheit} | {CPU_USAGE:<10.2f}% | {RUNNING_TIME:<10.1f} {RUNNING_UNIT}")

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