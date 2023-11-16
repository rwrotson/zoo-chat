from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db import update_db, delete_from_db
from app.exceptions import UserNotFound, UserAlreadyExists
from app import models, schemas


def get_all_users(session: Session) -> list[models.User]:
    a = list(session.execute(
        select(models.User)
    ).scalars().all())
    print(a, flush=True)
    return a


def get_user(session: Session, telegram_id: int) -> models.User:
    user = session.execute(
        select(models.User).
        filter_by(telegram_id=telegram_id)
    ).scalars().one_or_none()
    return user


def create_user(session: Session, user: schemas.User) -> models.User:
    if get_user(session=session, telegram_id=user.telegram_id):
        raise UserAlreadyExists()
    user_model = models.User(**user.dict())
    update_db(session, user_model)
    return user_model


def update_user(session: Session, user: schemas.User) -> models.User | None:
    user_model = get_user(session=session, telegram_id=user.telegram_id)
    if user_model:
        for key, value in vars(user).items():
            setattr(user_model, key, value)
        update_db(session, user_model)
    return user_model


def delete_user(session: Session, telegram_id: int) -> models.User | None:
    user_model = get_user(session=session, telegram_id=telegram_id)
    if user_model:
        delete_from_db(session, user_model)
    return user_model
