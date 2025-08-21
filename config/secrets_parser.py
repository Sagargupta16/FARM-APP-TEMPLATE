import yaml
import pymongo
from motor.motor_asyncio import AsyncIOMotorClient

# Function to parse secrets.yml file
with open("config/secrets.yml", "r") as stream:
    secrets = yaml.safe_load(stream)

# MongoDB secrets from secrets.yml file
mongodb_host = secrets["mongodb"]["host"]
mongodb_port = secrets["mongodb"]["port"]
mongodb_username = secrets["mongodb"].get("username")
mongodb_password = secrets["mongodb"].get("password")
mongodb_database = secrets["mongodb"].get("database", "farm_template")

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

#  Function to connect to MongoDB database (sync version for testing)
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
        # Test the connection
        sync_client.admin.command('ping')
        return sync_client
    except Exception as e:
        print(f"MongoDB connection error: {e}")
        return None

# Function to get MongoDB database
def get_mongodb_database():
    try:
        client = connect_to_mongodb()
        return client[mongodb_database]
    except Exception as e:
        print(e)
        return None
    

# Function to get MongoDB collection
def get_mongodb_collection(collection_name):
    try:
        database = get_mongodb_database()
        return database[collection_name]
    except Exception as e:
        print(e)
        return None
    
