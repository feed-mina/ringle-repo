import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from app.db.database import Base

class UsageHistory(Base):
    __tablename__ = "usage_history"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False)
    feature_name = Column(String, nullable=False)  # 'chat' or 'analysis'
    used_at = Column(DateTime, default=datetime.utcnow)

