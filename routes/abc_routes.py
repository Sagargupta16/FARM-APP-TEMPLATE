from fastapi import APIRouter, HTTPException
from models.abc_models import User, UserCreate
from services.abc_services import UserService
from typing import List

router = APIRouter()
user_service = UserService()

@router.get("/users", response_model=List[User])
async def get_users():
    """Get all users"""
    return await user_service.get_all_users()

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    """Get a user by ID"""
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=User)
async def create_user(user: UserCreate):
    """Create a new user"""
    return await user_service.create_user(user)

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    """Delete a user"""
    deleted = await user_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Delete this file if you don't want to use it. Use *_routes.py pattern to create new route files.