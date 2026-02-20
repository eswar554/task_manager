from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str
    deadline: datetime
    project_id: int
    assigned_to: int

class TaskUpdateStatus(BaseModel):
    status: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str

    class Config:
        from_attributes = True
