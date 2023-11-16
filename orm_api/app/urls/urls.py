from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.main import app
from app import crud, schemas
from app.db import get_session


@app.get('/compatibilities', response_model=list[schemas.Compatibility])
def get_all_compatibilities(db: Session = Depends(get_session())):
    compatibilities = crud.get_all_compatibilities(db)
    return compatibilities


@app.post('/compatibilities', response_model=schemas.Compatibility)
def add_compatibility(compatibility: schemas.Compatibility, db: Session = Depends(get_session())):
    db_compatibility = crud.get_compatibility(
        db, user_1=compatibility.user_1, user_2=compatibility.user_2
    )
    if db_compatibility:
        raise HTTPException(status_code=400, detail='compatibility already added')
    return crud.add_compatibility(db, compatibility)


@app.get('/compatibilities/{user_1}/{user_2}', response_model=schemas.Compatibility)
def get_compatibility(user_1: int, user_2: int, db: Session = Depends(get_session())):
    db_compatibility = crud.get_compatibility(db, user_1=user_1, user_2=user_2)
    if db_compatibility is None:
        raise HTTPException(status_code=404, detail='compatibility not found')
    return db_compatibility


@app.get('/pairings/{pair_type}', response_model=list[schemas.Pairing])
def get_optimal_pairs(pair_type: str, db: Session = Depends(get_session())):
    pairings = crud.get_all_pairings(db, pair_type)
    return pairings


@app.post('/pairings/', response_model=list[schemas.Pairing])
def rewrite_optimal_pairs(pairings: list[schemas.Pairing], db: Session = Depends(get_session())):
    pairings = crud.update_pairings(db, pairings)
    return pairings


@app.get('/triangles/{type_}', response_model=list[schemas.Triangle])
def get_optimal_triangles(type_: str, db: Session = Depends(get_session())):
    triangles = crud.get_all_pairings(db, type_)
    return triangles


@app.post('/triangles', response_model=list[schemas.Triangle])
def rewrite_optimal_triangles(triangles: list[schemas.Triangle], db: Session = Depends(get_session())):
    triangles = crud.update_triangles(db, triangles)
    return triangles
