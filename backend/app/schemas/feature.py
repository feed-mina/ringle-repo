from pydantic import BaseModel

class FeatureCreate(BaseModel):
    name: str
    description: str

class FeatureOut(FeatureCreate):
    class Config:
        from_attributes = True

