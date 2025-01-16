from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Endpoint : Lire les pandémies
@router.get("/pandemics", response_model=list[schemas.Pandemic])
def read_pandemics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_pandemics(db, skip=skip, limit=limit)

# Endpoint : Créer une pandémie
@router.post("/pandemics", response_model=schemas.Pandemic)
def create_pandemic(pandemic: schemas.PandemicCreate, db: Session = Depends(get_db)):
    return crud.create_pandemic(db, pandemic)