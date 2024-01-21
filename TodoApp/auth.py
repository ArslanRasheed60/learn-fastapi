from fastapi import APIRouter
from pydantic import BaseModel
from passlib.context import CryptContext
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.get("/auth/")
async def get_user():
    return {'user': 'authenticated'}

DB = []

bcrypt_context = CryptContext(schemes=['bcrypt'])

class User(BaseModel):
    username: str
    password: str


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    DB.append({
        'username': user.username,
        'password': bcrypt_context.hash(user.password)
    })
    return DB

@router.post("/token", status_code=status.HTTP_201_CREATED)
async def login_for_access_token():
    pass