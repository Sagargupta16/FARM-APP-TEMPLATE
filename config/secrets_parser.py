import yaml
import pymongo

# Function to parse secrets.yml file
with open("config/secrets.yml", "r") as stream:
    secrets = yaml.safe_load(stream)

# MongoDB secrets from secrets.yml file
mongodb_host = secrets["mongodb"]["host"]
mongodb_port = secrets["mongodb"]["port"]
mongodb_username = secrets["mongodb"]["username"]
mongodb_password = secrets["mongodb"]["password"]
mongodb_database = secrets["mongodb"]["database"]


#  Function to connect to MongoDB database
def connect_to_mongodb():
    try:
        client = pymongo.MongoClient(
            host=mongodb_host,
            port=mongodb_port,
            username=mongodb_username,
            password=mongodb_password,
            authSource=mongodb_database,
            authMechanism="SCRAM-SHA-256",
        )
        return client
    except Exception as e:
        print(e)
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
    
