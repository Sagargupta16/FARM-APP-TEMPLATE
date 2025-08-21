from motor.motor_asyncio import AsyncIOMotorClient
from models.abc_models import User, UserCreate
from config.secrets_parser import get_database
from bson import ObjectId
from datetime import datetime
from typing import List, Optional

class UserService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.users

    async def get_all_users(self) -> List[User]:
        """Get all users from database"""
        users = []
        async for user in self.collection.find():
            user["id"] = str(user["_id"])
            del user["_id"]
            users.append(User(**user))
        return users

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get a user by ID"""
        try:
            user = await self.collection.find_one({"_id": ObjectId(user_id)})
            if user:
                user["id"] = str(user["_id"])
                del user["_id"]
                return User(**user)
        except Exception:
            return None
        return None

    async def create_user(self, user_data: UserCreate) -> User:
        """Create a new user"""
        user_dict = user_data.dict()
        user_dict["created_at"] = datetime.now()
        
        result = await self.collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)
        
        return User(**user_dict)

    async def delete_user(self, user_id: str) -> bool:
        """Delete a user by ID"""
        try:
            result = await self.collection.delete_one({"_id": ObjectId(user_id)})
            return result.deleted_count > 0
        except Exception:
            return False

# Delete this file if you don't want to use it. Use *_service.py pattern to create new service files.
