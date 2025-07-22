from app.models.feature import Feature
from sqlalchemy.orm import Session
from app.schemas.feature import FeatureCreate

def create_feature(db: Session, data: FeatureCreate):
    feature = Feature(**data.dict())
    db.add(feature)
    db.commit()
    db.refresh(feature)
    return feature

