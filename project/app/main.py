from fastapi import FastAPI
from app.routes import api
from app.database import Base, engine

# Initialisation de l'application FastAPI
app = FastAPI()

# Création des tables dans la base si elles n'existent pas
Base.metadata.create_all(bind=engine)

# Inclusion des routes
app.include_router(api.router)