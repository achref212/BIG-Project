from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

DATABASE_URL = (
    settings.database_url
    or f"postgresql+psycopg2://{settings.db_user}:"
       f"{settings.db_password}@{settings.db_host}:"
       f"{settings.db_port}/{settings.db_name}"
)

engine = create_engine(DATABASE_URL, echo=settings.debug)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
