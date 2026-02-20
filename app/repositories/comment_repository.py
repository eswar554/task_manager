from sqlalchemy.orm import Session
from app.models.comment_model import Comment


def create_comment(db: Session, data):
    comment = Comment(**data)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comments_by_task(db: Session, task_id: int):
    return db.query(Comment).filter(Comment.task_id == task_id).all()
