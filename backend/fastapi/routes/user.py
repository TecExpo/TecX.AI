from fastapi import APIRouter, HTTPException, Depends
from models import User
from typing import List

router = APIRouter()

users_db = []

@router.get("/", response_model=List[User])
async def get_users():
    return users_db

@router.post("/")
async def create_user(user: User):
    users_db.append(user)
    return {"message": "User created successfully", "user": user}
