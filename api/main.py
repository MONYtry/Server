from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from Server.overview import getDisk, getNetwork,getRAM,getUptime
load_dotenv()
import psutil

BACKEND_URL = os.getenv("BACKEND_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL")

# Erstellung der API
app = FastAPI()

# Einstellung der API
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://127.0.0.1:5500"],
                   allow_methods=["*"],
                   allow_headers=["*"],
                   allow_credentials=True)

@app.get("/")
def home():
    return {"message": "API läufteee"}

@app.get("/home")
def home():
    return {"message": "Home sweet home"}

old_net = psutil.net_io_counters()

@app.get("/monitor")
def monitor():
    RAM_FREE, RAM_TOTAL, RAM_USED = getRAM()
    DISK_FREE, DISK_PERCENT, DISK_TOTAL, DISK_USAGE = getDisk()
    SECONDS, MINUTES, HOURS = getUptime()
    NET, UPLOAD_SPEED, DOWNLOAD_SPEED = getNetwork(old_net,5)

    return {
        "ram_free": f"{RAM_FREE:.2f}",
        "ram_total": f"{RAM_TOTAL:.2f}",
        "ram_used": f"{RAM_USED:.2f}",
        "disk_free": f"{DISK_FREE:.2f}",
        "disk_percent": f"{DISK_PERCENT:.2f}",
        "disk_total": f"{DISK_TOTAL:.2f}",
        "disk_usage": f"{DISK_USAGE:.2f}",
        "uptime": f"{HOURS}h {MINUTES}min {SECONDS}s",
        "upload_speed": f"{UPLOAD_SPEED:.2f}",
        "download_speed": f"{DOWNLOAD_SPEED:.2f}"
    }

