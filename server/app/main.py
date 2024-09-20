import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
import dotenv

# Load environment variables from the .env file
dotenv.load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)


# Root endpoint for basic health check
@app.get("/")
async def root():
    return {"message": "Welcome to the API"}


# Debug endpoint to check server status
@app.get("/debug")
async def debug():
    return {"status": "Running", "message": "Debug information available"}


# Demo POST endpoint
@app.post("/demo")
async def demo(message: str):
    """
    Echoes the message provided in the request body.
    """
    return {"message": message}


# Config endpoint to retrieve environment configuration
@app.get("/config")
async def get_config():
    """
    Returns the current configuration based on environment variables.
    """
    return {
        "app_env": os.getenv("APP_ENV", "Not Set"),
        "debug": os.getenv("DEBUG", "Not Set"),
        "database_url": os.getenv("DATABASE_URL", "Not Set"),
        "openai_api_key": os.getenv("OPENAI_API_KEY", "Not Set"),
        "other_api_key": os.getenv("OTHER_API_KEY", "Not Set"),
    }
