from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes.abc_routes import router as abc_router
import os

app = FastAPI(
    title="FARM App Template",
    description="A simple FARM (FastAPI, React, MongoDB) stack template",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(abc_router, prefix="/api/v1", tags=["example"])

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "FARM App Template is running"}

# Only mount static files if the client_build directory exists
if os.path.exists("client_build"):
    app.mount("/", StaticFiles(directory="client_build", html=True), name="frontend")
else:
    @app.get("/")
    async def root():
        return {"message": "FARM App Template - React frontend not built yet. Run 'npm run build' in the client directory first."}
