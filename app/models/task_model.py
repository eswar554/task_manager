from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(255))

    status = Column(String(50), default="todo")  # todo, in_progress, done
    priority = Column(String(50))  # low, medium, high

    deadline = Column(DateTime)

    project_id = Column(Integer, ForeignKey("projects.id"))
    assigned_to = Column(Integer, ForeignKey("users.id"))

    project = relationship("Project")
    user = relationship("User")
