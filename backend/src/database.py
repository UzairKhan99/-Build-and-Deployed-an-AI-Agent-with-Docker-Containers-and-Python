import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine

import models


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("MYSQL_URL")

if DATABASE_URL is None:
    raise RuntimeError("Database URL is missing")

if DATABASE_URL.startswith("mysql://"):
    DATABASE_URL = DATABASE_URL.replace("mysql://", "mysql+pymysql://", 1)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)