from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db import update_db, delete_from_db
from app import models, schemas


def get_all_compatibilities(session: Session) -> list[models.Compatibility]:
    return list(session.execute(
        select(models.Compatibility)
    ).scalars().all())


def get_compatibility(session: Session, user_1_id: int, user_2_id: int) -> models.Compatibility | None:
    return session.execute(
        select(models.Compatibility).
        filter_by(user_1_id=user_1_id, user_2_id=user_2_id)
    ).scalars().first()


def add_compatibility(session: Session, compatibility: schemas.Compatibility) -> models.Compatibility:
    db_compatibility = models.Compatibility(**compatibility.dict())
    db_compatibility_inversed = models.Compatibility(
        **compatibility.dict(),
        user_1=compatibility.user_2,
        user_2=compatibility.user_1
    )
    update_db(session, db_compatibility, db_compatibility_inversed)
    return db_compatibility