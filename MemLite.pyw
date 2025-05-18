import os
import psutil
import time
import platform
from datetime import datetime
import threading

LOG_FILE = os.path.expanduser("~/Desktop/memory_log.txt")

def log_sys_info():
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- {datetime.now()} ---\n")

        mem = psutil.virtual_memory()
        f.write(f"Total RAM: {mem.total / 1e9:.2f} GB\n")
        f.write(f"Used RAM: {mem.used / 1e9:.2f} GB ({mem.percent}%)\n")
        f.write(f"Available RAM: {mem.available / 1e9:.2f} GB\n")

        swap = psutil.swap_memory()
        f.write(f"Swap Used: {swap.used / 1e9:.2f} GB ({swap.percent}%)\n")

        f.write(f"CPU Usage: {psutil.cpu_percent()}%\n")
        f.write(f"Load Avg (1/5/15 min): {os.getloadavg()}\n")

        if platform.system() == "Darwin":
            gpu_info = os.popen("system_profiler SPDisplaysDataType | grep 'VRAM'").read()
            f.write(f"GPU VRAM Info: {gpu_info.strip()}\n")

        f.flush()

def start_monitor():
    while True:
        log_sys_info()
        time.sleep(10)

threading.Thread(target=start_monitor, daemon=True).start()

# Keep the script running in background without showing a window
while True:
    time.sleep(60)