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
        "ram_free": RAM_FREE,
        "ram_total": RAM_TOTAL,
        "ram_used": RAM_USED,
        "disk_free": DISK_FREE,
        "disk_percent": DISK_PERCENT,
        "disk_total": DISK_TOTAL,
        "disk_usage": DISK_USAGE,
        "uptime": str(HOURS) + "h " + str(MINUTES) + "min " + str(SECONDS) + "s",
        "upload_speed": UPLOAD_SPEED,
        "download_speed": DOWNLOAD_SPEED
            }
