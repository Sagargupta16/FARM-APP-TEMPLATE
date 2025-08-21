from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Delete this file if you don't want to use it. Use *_model.py pattern to create new model files.