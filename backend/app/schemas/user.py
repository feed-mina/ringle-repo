from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: str
    name: str

class UserOut(BaseModel):
    id: str
    email: str
    name: str
    created_at: Optional[datetime]

    class Config:
        from_attributes = True

