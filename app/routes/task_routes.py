from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.task_schema import TaskCreate, TaskUpdateStatus
from app.utils.dependencies import get_db
from app.controllers.task_controller import (
    create_task_controller,
    get_tasks_controller,
    update_status_controller,
    filter_tasks_controller,
    search_tasks_controller
)
from fastapi import Query


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_controller(task, db)


@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return get_tasks_controller(db)


@router.patch("/{task_id}/status")
def update_task_status(task_id: int, status: TaskUpdateStatus, db: Session = Depends(get_db)):
    return update_status_controller(task_id, status, db)


@router.get("/filter")
def filter_tasks(
    status: str = None,
    priority: str = None,
    project_id: int = None,
    db: Session = Depends(get_db)
):
    return filter_tasks_controller(status, priority, project_id, db)

@router.get("/search")
def search_tasks(keyword: str, db: Session = Depends(get_db)):
    return search_tasks_controller(keyword, db)
