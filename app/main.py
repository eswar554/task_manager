from fastapi import FastAPI #Imports FastAPI framework. Used to create the web API server.
from app.database import Base, engine #parent class for all SQLAlchemy models. database connection object.
# import ALL models so tables are created
from app.models import user_model
from app.models import project_model
from app.models import task_model
from app.models import comment_model
from app.models import activity_model
# import routers
from app.routes import auth_routes, project_routes, task_routes, comment_routes
# middleware
from app.utils.middleware import log_requests
# create table
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Task Manager API")

# register routers
app.include_router(auth_routes.router)
app.include_router(project_routes.router)
app.include_router(task_routes.router)
app.include_router(comment_routes.router)

# middleware
app.middleware("http")(log_requests)

@app.get("/")
def home():
    return {"message": "Task Manager API running 🚀"}
