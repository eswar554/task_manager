from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.comment_repository import create_comment, get_comments_by_task
from app.repositories.activity_repository import log_activity


def add_comment_controller(comment, db: Session):

    new_comment = create_comment(db, comment.dict())

    log_activity(
        db,
        action="Comment added",
        task_id=comment.task_id,
        user_id=comment.user_id
    )

    return {"message": "Comment added successfully"}


def get_comments_controller(task_id: int, db: Session):

    comments = get_comments_by_task(db, task_id)

    if not comments:
        raise HTTPException(status_code=404, detail="No comments found")

    return comments
