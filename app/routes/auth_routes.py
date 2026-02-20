from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.testing.plugin.plugin_base import post

from app.schemas.user_schema import UserCreate, UserLogin
from app.utils.dependencies import get_db
from app.controllers.auth_controller import (
    register_user_controller,
    login_user_controller
)

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user_controller(user, db)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user_controller(user, db)
