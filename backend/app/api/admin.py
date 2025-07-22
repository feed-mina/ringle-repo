from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas import membership as schemas
from app.crud import membership as crud
from app.schemas import user_membership as um_schemas
from app.crud import user_membership as um_crud
from app.models.user_membership import UserMembership

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/memberships", response_model=schemas.MembershipOut)
def create_membership(data: schemas.MembershipCreate, db: Session = Depends(get_db)):
    return crud.create_membership(db, data)

@router.get("/memberships", response_model=list[schemas.MembershipOut])
def list_memberships(db: Session = Depends(get_db)):
    return crud.get_memberships(db)




@router.post("/assign", response_model=um_schemas.UserMembershipOut)
def assign_membership(data: um_schemas.UserMembershipAssignRequest, db: Session = Depends(get_db)):
    return um_crud.assign_membership(db, data)


@router.get("/user/debug")
def debug_memberships(db: Session = Depends(get_db)):
    return db.query(UserMembership).all()

