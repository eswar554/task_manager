from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.user_repository import get_user_by_email, create_user
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

def register_user_controller(user, db: Session):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)
    new_user = create_user(db, user.name, user.email, hashed_password)
    return {"message": "User created successfully", "user_id": new_user.id}


def login_user_controller(user, db: Session):
    db_user = get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
