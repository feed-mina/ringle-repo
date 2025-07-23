from fastapi import FastAPI
from app.api import admin, user
from app.models import membership
from app.db.database import Base, engine
from app.models import user_membership
from app.models import usage_history
from app.models import user
from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin.router, prefix="/admin")
app.include_router(user.router, prefix="/user")
