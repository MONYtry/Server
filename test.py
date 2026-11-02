
import psutil
import time

print(f"{'PID':<8} {'Prozessname':<20}")
print("-" * 31)

processes = []

# Geht durch alle Prozesse
# Fügt sie dem Array hinzu
for p in psutil.process_iter(["pid", "name"]):
    processes.append(p)
    
# Sortiert den Array nach Memory-Usage
# Umgedreht = Von höchste zu niedrigste
processes = sorted(processes, key=lambda p: p.memory_info().rss / (1024**2), reverse=True)

# Unsere Hauptfunktion 
for p in processes:
    einheit = "MB"
    einheit_time = 0
    einheit_time_display = "sec"
    
    CPU_USAGE = p.cpu_percent()
    RAM_USAGE = p.memory_info().rss / (1024**2)

    RUNNING_SECONDS = time.time() - p.create_time() 
    RUNNING_MINUTES = RUNNING_SECONDS / 60
    RUNNING_HOURS = RUNNING_MINUTES / 60
    
    if RUNNING_SECONDS < 60:
        einheit_time = RUNNING_SECONDS
        einheit_time_display = "sec"

    elif RUNNING_MINUTES < 60:
        einheit_time = RUNNING_MINUTES
        einheit_time_display = "min"

    else:
        einheit_time = RUNNING_HOURS
        einheit_time_display = "hrs"

    if RAM_USAGE >= 1000:
        einheit = "GB"

    print(f"{p.info['pid']:<8} | {p.info['name']:<25} | {RAM_USAGE:<10.2f} {einheit} | {CPU_USAGE:<10.2f}% | {einheit_time:<10.1f} {einheit_time_display}")
