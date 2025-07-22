# app/schemas/use_feature.py

from pydantic import BaseModel

class UseFeatureRequest(BaseModel):
    user_id: str
    feature_name: str

class UseFeatureResponse(BaseModel):
    success: bool
    message: str
    remaining_count: int | None = None

