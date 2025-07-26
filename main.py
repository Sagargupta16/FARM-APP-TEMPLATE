from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Only mount static files if the client_build directory exists
if os.path.exists("client_build"):
    app.mount("/", StaticFiles(directory="client_build", html=True), name="frontend")
else:
    @app.get("/")
    async def root():
        return {"message": "FARM App Template - React frontend not built yet. Run 'npm run build' in the client directory first."}
