from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas.user import UserCreate, UserResponse, Token
from app.services.user import create_user, get_users
from app.services.auth import register_user,UserLogin,login_user, forgot_password, reset_password

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)


# Register new user
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = register_user(db, user)
    return db_user

# Login user
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user)

@router.post("/forgot-password")
async def forgot_password_request(email: str, db: Session = Depends(get_db)):
    return await forgot_password(db, email)

@router.post("/reset-password")
def reset_password_request(token: str, new_password: str, db: Session = Depends(get_db)):
    return reset_password(db, token, new_password)