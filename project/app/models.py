from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Exemple de table : Pandémies
class Pandemic(Base):
    __tablename__ = "pandemics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    year = Column(Integer)
    mortality_rate = Column(Float)