from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.task_repository import get_tasks_paginated

from app.repositories.task_repository import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task_status
)
from app.repositories.task_repository import filter_tasks
from app.repositories.task_repository import search_tasks

def create_task_controller(task, db: Session):
    new_task = create_task(db, task.dict())
    return {
        "message": "Task created successfully",
        "task_id": new_task.id
    }


def get_tasks_controller(db: Session):
    tasks = get_tasks(db)
    return tasks


def update_status_controller(task_id: int, status_data, db: Session):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = update_task_status(db, task, status_data.status)
    return {
        "message": "Task status updated",
        "task_status": updated_task.status
    }


def filter_tasks_controller(status, priority, project_id, db):
    tasks = filter_tasks(db, status, priority, project_id)
    return tasks

def search_tasks_controller(keyword, db):
    return search_tasks(db, keyword)