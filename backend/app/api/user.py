from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.crud import user_membership
from app.schemas.user_membership import UserMembershipStatusOut
import app.crud.use_feature as feature_crud
from app.schemas.use_feature import UseFeatureRequest, UseFeatureResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/membership", response_model=UserMembershipStatusOut)
def get_user_membership(user_id: str, db: Session = Depends(get_db)):
    result = user_membership.get_user_membership_status(db, user_id)
    if result is None:
        return {"detail": "No active membership found"}
    return result



@router.post("/use-feature", response_model=UseFeatureResponse)
def use_feature_endpoint(data: UseFeatureRequest, db: Session = Depends(get_db)):
    success, message, remaining = feature_crud.use_feature(db, data.user_id, data.feature_name)
    return UseFeatureResponse(
        success=success,
        message=message,
        remaining_count=remaining
    )

