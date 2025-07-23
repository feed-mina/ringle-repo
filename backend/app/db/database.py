from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)


print(".env env_path",env_path)
print(".env exit?", env_path.exists())
print(".env 위치:", os.path.join(os.path.dirname(__file__), '..', '.env')) 
print("DATABASE_URL =", os.getenv("DATABASE_URL")) 
#load_dotenv()
#load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


DATABASE_URL = os.getenv("DATABASE_URL")

#engine = create_engine(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

