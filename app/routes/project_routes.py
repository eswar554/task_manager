from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.project_schema import ProjectCreate
from app.utils.dependencies import get_db
from app.controllers.project_controller import (
    create_project_controller,
    get_projects_controller
)

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project_controller(project, db)


@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return get_projects_controller(db)
