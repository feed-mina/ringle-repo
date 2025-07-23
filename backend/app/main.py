from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.api import admin
from app.api import user
from app.models import membership
from app.db.database import Base
from app.db.database import engine
from app.models import user_membership
from app.models import usage_history
from app.models import user as user_model
from dotenv import load_dotenv
from pathlib import Path
import os
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
os.environ["PGCLIENCODING"] = "utf8"

#load_dotenv()
#load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

load_dotenv(dotenv_path=env_path)

print("DATABASE_URL:", os.getenv("DATABASE_URL"))

Base.metadata.create_all(bind=engine)

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
