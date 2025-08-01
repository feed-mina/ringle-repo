# 파일: schemas/user_membership.py
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import List

class UserMembershipAssignRequest(BaseModel):
    user_id: str
    membership_id: UUID

class UserMembershipOut(BaseModel):
    id: UUID
    user_id: str
    membership_id: UUID
    start_date: datetime
    end_date: datetime

    class Config:
        from_attributes = True


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

