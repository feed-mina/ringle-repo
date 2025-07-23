from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.crud import user_membership
from app.schemas.user_membership import UserMembershipStatusOut
import app.crud.use_feature as feature_crud
from app.schemas.use_feature import UseFeatureRequest, UseFeatureResponse
from app.schemas.chat import ChatRequest, ChatResponse
from app.crud.chat import generate_chat_response
from app.schemas.payment import MockPaymentRequest
from app.crud.user_membership import assign_membership
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


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(data: ChatRequest):
    response = generate_chat_response(data.message)
    return ChatResponse(response=response)



@router.post("/mock/payment")
def mock_payment(data: MockPaymentRequest, db: Session = Depends(get_db)):
    new_membership = assign_membership(db, data)
    return {"message": "멤버십 부여 완료", "membership_id": new_membership.membership_id}

