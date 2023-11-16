from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db import update_db, delete_from_db
from app import models, schemas


def get_all_triangles(session: Session, triangle_type: str) -> list[models.Triangle]:
    return list(session.execute(
        select(models.Triangle).
        filter_by(type=triangle_type)
    ).scalars().all())


def update_triangles(session: Session, triangles: list[schemas.Triangle]):
    session.query(models.Triangle).delete()
    session.add_all([models.Triangle(**triangle.dict()) for triangle in triangles])
    session.commit()
    return session.query(models.Triangle).all()