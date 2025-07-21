from fastapi import FastAPI
from app.api import admin
from app.models import membership
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin.router, prefix="/admin")

