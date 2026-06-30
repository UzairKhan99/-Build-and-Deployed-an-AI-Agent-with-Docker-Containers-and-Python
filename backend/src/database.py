import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine

from models import AgentRun

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not configured")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def init_db() -> None:
    SQLModel.metadata.create_all(engine)
