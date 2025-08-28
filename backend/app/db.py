from sqlmodel import SQLModel, create_engine, Session

from app.core import settings

engine = create_engine(settings.settings.DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)