from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine(
    settings.database_url,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
