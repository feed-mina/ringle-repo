# models/membership_feature.py
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

class MembershipFeature(Base):
    __tablename__ = "membership_features"

    id = Column(String, primary_key=True, index=True)
    membership_id = Column(String, ForeignKey("memberships.id"))
    feature_id = Column(String, ForeignKey("features.id"))
    usage_limit = Column(Integer)

    membership = relationship("Membership", back_populates="features")
    feature = relationship("Feature")

