from sqlalchemy import create_engine #create_engine → connects Python to the database.
from sqlalchemy.orm import sessionmaker, declarative_base #sessionmaker → creates database sessions (used for queries). -> declarative_base → base class for creating ORM models.
from app.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME #Imports DB credentials from config file.

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL) #Creates database connection engine.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Creates a session factory.

Base = declarative_base() #Parent class for all database models.
