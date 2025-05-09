from fastapi import APIRouter, HTTPException, Depends
from models.user import User
from db import db
from utils import hash_password, verify_password, create_token


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(user: User):
    user_exists = await db.users.find_one({"email": user.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="User already exists")
    user.password = hash_password(user.password)
    await db.users.insert_one(user.dict())
    return {"msg": "user created successfully"}


@router.post("/login")
async def login(user: User):
    db_user = await db.users.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": user.email})
    return {"access_token": token}


