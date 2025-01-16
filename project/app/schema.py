from pydantic import BaseModel

# Exemple de schéma Pydantic
class PandemicBase(BaseModel):
    name: str
    year: int
    mortality_rate: float

class PandemicCreate(PandemicBase):
    pass

class Pandemic(PandemicBase):
    id: int

    class Config:
        orm_mode = True