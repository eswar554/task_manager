from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.project_repository import (
    create_project,
    get_all_projects
)


def create_project_controller(project, db: Session):

    new_project = create_project(
        db,
        project.name,
        project.description,
        project.owner_id
    )

    return {
        "message": "Project created successfully",
        "project_id": new_project.id
    }


def get_projects_controller(db: Session):

    projects = get_all_projects(db)

    return projects
