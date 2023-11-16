from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db import update_db, delete_from_db
from app import models, schemas


def get_all_pairings(session: Session, pair_type: str) -> list[models.Pairing]:
    return list(session.execute(
        select(models.Pairing).
        filter(models.Pairing.type == pair_type)
    ).scalars().all())


def update_pairings(session: Session, pairings: list[schemas.Pairing]):
    session.query(models.Pairing).delete()
    update_db(*[models.Pairing(**pairing.dict()) for pairing in pairings])
    return session.query(models.Pairing).all()
