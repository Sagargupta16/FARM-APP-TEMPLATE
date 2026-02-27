import os
import yaml
import pymongo
from pathlib import Path
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# Load config from secrets.yml as fallback defaults
config_path = Path(__file__).parent / "secrets.yml"
with open(config_path, "r") as stream:
    secrets = yaml.safe_load(stream)

# Prefer environment variables, fall back to secrets.yml
mongodb_host = os.getenv("MONGODB_HOST", secrets["mongodb"]["host"])
mongodb_port = int(os.getenv("MONGODB_PORT", secrets["mongodb"]["port"]))
mongodb_username = os.getenv("MONGODB_USERNAME", secrets["mongodb"].get("username"))
mongodb_password = os.getenv("MONGODB_PASSWORD", secrets["mongodb"].get("password"))
mongodb_database = os.getenv("MONGODB_DATABASE", secrets["mongodb"].get("database", "farm_template"))

# Connection string for MongoDB
if mongodb_username and mongodb_password:
    MONGODB_URL = f"mongodb://{mongodb_username}:{mongodb_password}@{mongodb_host}:{mongodb_port}/{mongodb_database}"
else:
    MONGODB_URL = f"mongodb://{mongodb_host}:{mongodb_port}"

# Async MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)

def get_database():
    """Get the database instance"""
    return client[mongodb_database]

# Function to connect to MongoDB database (sync version for testing)
def connect_to_mongodb():
    try:
        sync_client = pymongo.MongoClient(
            host=mongodb_host,
            port=mongodb_port,
            username=mongodb_username,
            password=mongodb_password,
            authSource=mongodb_database if mongodb_username else None,
            authMechanism="SCRAM-SHA-256" if mongodb_username else None,
        )
        sync_client.admin.command('ping')
        return sync_client
    except Exception as e:
        print(f"MongoDB connection error: {e}")
        return None

def get_mongodb_database():
    try:
        db_client = connect_to_mongodb()
        return db_client[mongodb_database]
    except Exception as e:
        print(e)
        return None

def get_mongodb_collection(collection_name):
    try:
        database = get_mongodb_database()
        return database[collection_name]
    except Exception as e:
        print(e)
        return None
