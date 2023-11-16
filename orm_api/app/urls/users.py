from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_session
from app import schemas
from app.crud import users


router = APIRouter()


@router.get('/users', response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_session)):  # нужна ли тут сессия??
    all_users = users.get_all_users(db)
    return all_users


@router.post('/users', response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_session)):
    db_user = users.get_user(db, telegram_id=user.telegram_id)
    if db_user:
        raise HTTPException(status_code=400, detail='User already added')
    return users.create_user(session=db, user=user)


@router.get('/users/{telegram_id}', response_model=schemas.User)
def get_user(telegram_id: int, db: Session = Depends(get_session)):
    db_user = users.get_user(db, telegram_id=telegram_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='user not found')
    return db_user


@router.patch('/users/{telegram_id}', response_model=schemas.User)
def update_user(telegram_id: int, user: schemas.User, db: Session = Depends(get_session)):
    db_user = users.get_user(db, telegram_id=telegram_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='user not found')
    return users.update_user(db, user)


@router.delete('/users/{telegram_id}', response_model=schemas.User)
def delete_user_and_all_compatibilities(telegram_id: int, db: Session = Depends(get_session)):
    db_user = users.get_user(db, telegram_id=telegram_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='user not found')
    return users.delete_user(db, telegram_id=telegram_id)
