from typing import List
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class FeatureStatus(BaseModel):
    feature_name: str
    used_count: int
    remaining_count: int

class UserMembershipStatusOut(BaseModel):
    membership_name: str
    start_date: datetime
    end_date: datetime
    features: List[FeatureStatus]

    class Config:
        from_attributes = True

