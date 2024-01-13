from fastapi import APIRouter
from pydantic import BaseModel
from passlib.context import CryptContext

router = APIRouter()

@router.get("/auth/")
async def get_user():
    return {'user': 'authenticated'}

DB = []

class User(BaseModel):
    username: str
    password: str


@router.post("/auth")
async def create_user(user: User):
    return user