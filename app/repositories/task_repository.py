from sqlalchemy.orm import Session
from app.models.task_model import Task


def create_task(db: Session, task_data):
    task = Task(**task_data)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task_status(db: Session, task, status: str):
    task.status = status
    db.commit()
    db.refresh(task)
    return task


def filter_tasks(db, status=None, priority=None, project_id=None):
    query = db.query(Task)
    if status:
        query = query.filter(Task.status == status)
    if priority:
        query = query.filter(Task.priority == priority)
    if project_id:
        query = query.filter(Task.project_id == project_id)
    return query.all()

def search_tasks(db, keyword: str):
    return db.query(Task).filter(Task.title.ilike(f"%{keyword}%")).all()
