from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def init_db():
    """
    Creates all tables if the SQLite file (app.db) does not exist.
    You can expand this to check migrations later.
    """
    from . import models  # Import models so Base.metadata is populated
    Base.metadata.create_all(engine)
