from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.comment_schema import CommentCreate
from app.utils.dependencies import get_db
from app.controllers.comment_controller import (
    add_comment_controller,
    get_comments_controller
)

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/")
def add_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return add_comment_controller(comment, db)


@router.get("/task/{task_id}")
def get_comments(task_id: int, db: Session = Depends(get_db)):
    return get_comments_controller(task_id, db)
