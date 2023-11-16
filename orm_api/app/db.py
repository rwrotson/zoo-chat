from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.consts import SQLALCHEMY_DB_URL
from app.models import Base


engine = create_engine(SQLALCHEMY_DB_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def update_db(session: Session, *objs: Base) -> None:
    session.add_all(objs)
    session.commit()


def delete_from_db(session: Session, *objs: Base) -> None:
    for obj in objs:
        session.delete(obj)
    session.commit()
