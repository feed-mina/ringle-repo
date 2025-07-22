# app/models/feature.py
from sqlalchemy import Column, String
from app.db.database import Base

class Feature(Base):
    __tablename__ = "features"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)

