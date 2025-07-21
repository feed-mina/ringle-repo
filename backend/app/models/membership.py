import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Membership(Base):
    __tablename__ = "memberships"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    duration_days = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    features = relationship("MembershipFeature", back_populates="membership")


class MembershipFeature(Base):
    __tablename__ = "membership_features"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    membership_id = Column(String, ForeignKey("memberships.id"), nullable=False)
    feature_name = Column(String, nullable=False)  # 'chat' or 'analysis'
    limit_count = Column(Integer, nullable=False)  # -1 means unlimited

    membership = relationship("Membership", back_populates="features")

