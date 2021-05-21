from fastapi import (
    APIRouter,
    Depends,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import models, tables
from ..core.base import get_db
from ..services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post(
    '/sign-up/',
    response_model=models.Token,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(
    user_data: models.UserCreate,
    auth_service: AuthService = Depends(),
):
    return auth_service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=models.Token,
)
def sign_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
):
    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )


@router.get(
    '/user/',
    response_model=models.User,
)
def get_user(user: models.User = Depends(get_current_user)):
    return user

@router.post("/create_question")
def create_answer(
    details: models.QuestionCreate,
    db: Session = Depends(get_db),
):
    to_create = tables.Question(
        # id=details.id,
        text_question=details.text_question,
    )
    db.add(to_create)
    db.commit()
    return to_create

@router.get("/get_question")
def get_question(
        id: int,
        db: Session = Depends(get_db)
):
    return db.query(tables.Question).filter(tables.Question.id == id).first()
