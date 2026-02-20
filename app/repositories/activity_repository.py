from sqlalchemy.orm import Session
from app.models.activity_model import ActivityLog


def log_activity(db: Session, action: str, task_id: int, user_id: int):
    activity = ActivityLog(
        action=action,
        task_id=task_id,
        user_id=user_id
    )
    db.add(activity)
    db.commit()
