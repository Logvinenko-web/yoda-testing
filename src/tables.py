from sqlalchemy import (
    Column,
    Integer,
    String,
)

from src.core.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password_hash = Column(String)


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    text_question = Column(String)
