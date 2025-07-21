from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

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

