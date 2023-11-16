from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db import update_db, delete_from_db
from app.exceptions import BestiaryAlreadyExists, BestiaryNotFound, UserNotFound
from app.crud.users import get_user
from app import models, schemas


def _get_bestiary(session: Session, title: str) -> models.Bestiary | None:
    return session.execute(
        select(models.Bestiary).
        filter_by(title=title)
    ).scalars().one_or_none()


def create_bestiary(session: Session, bestiary: schemas.Bestiary) -> models.Bestiary:
    if _get_bestiary(session=session, title=bestiary.title):
        raise BestiaryAlreadyExists()
    bestiary_model = models.Bestiary(
        title=bestiary.title,
        password=bestiary.password,
        creator=bestiary.creator_tg_id
    )
    update_db(session, bestiary_model)
    return bestiary_model


def add_to_bestiary(session: Session, bestiary_title: str, user_telegram_id: int) -> models.Bestiary:
    bestiary = _get_bestiary(session=session, title=bestiary_title)
    if not bestiary:
        raise BestiaryNotFound()
    user = get_user(session=session, telegram_id=user_telegram_id)
    bestiary.members.append(user)
    update_db(session, bestiary)


def get_password_to_bestiary(session: Session, bestiary_title: str) -> str:
    bestiary = _get_bestiary(session=session, title=bestiary_title)
    if not bestiary:
        raise BestiaryNotFound()
    return bestiary.password
