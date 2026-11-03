import uvicorn
from api.main import app

# BACKEND-Angaben
IP = "0.0.0.0"
PORT = 8000

def start_service():
    # Configuration of the Server
    config = uvicorn.Config(app, host=IP, port=PORT)
    
    # Connecting the Config to the Server
    server = uvicorn.Server(config)
    
    # Starting the Server
    server.run()

if __name__ == "__main__":
    start_service()