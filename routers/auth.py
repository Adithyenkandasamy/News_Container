from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from utils.jwt_handler import create_jwt_token

router = APIRouter()

users_db = {}  # temporary in-memory user store

class User(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User exists")
    users_db[user.username] = user.password
    return {"message": "User registered"}

@router.post("/login")
def login(user: User):
    if users_db.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="Invalid login")
    token = create_jwt_token(user.username)
    return {"access_token": token}
