from sqlalchemy.orm import Session
from app import models, schemas

# Créer une nouvelle pandémie
def create_pandemic(db: Session, pandemic: schemas.PandemicCreate):
    db_pandemic = models.Pandemic(**pandemic.dict())
    db.add(db_pandemic)
    db.commit()
    db.refresh(db_pandemic)
    return db_pandemic

# Lire toutes les pandémies
def get_pandemics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pandemic).offset(skip).limit(limit).all()