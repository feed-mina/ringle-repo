from typing import List, Literal, Optional
from pydantic import BaseModel
from datetime import datetime

class MembershipFeatureCreate(BaseModel):
    feature_name: Literal["chat", "analysis"]
    limit_count: int

class MembershipCreate(BaseModel):
    name: str
    duration_days: int
    features: List[MembershipFeatureCreate]

class MembershipFeatureOut(MembershipFeatureCreate):
    id: str

class MembershipOut(BaseModel):
    id: str
    name: str
    duration_days: int
    created_at: datetime
    features: List[MembershipFeatureOut]

    class Config:
        from_attributes = True

