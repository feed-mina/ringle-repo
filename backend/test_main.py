import os
import sys
from dotenv import load_dotenv
sys.path.append(os.path.join(os.path.dirname(__file__),"app"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from api import admin, user
from models import membership
from db.database import Base, engine
from models import user_membership
from models import usage_history
from models import user


load_dotenv()
print("DATABASE_URL:", os.getenv("DATABASE_URL"))
print("Tables to be created:", Base.metadata.tables.keys())

# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:5173"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
    )

app.include_router(admin.router, prefix="/admin")
app.include_router(user.router, prefix="/user")
