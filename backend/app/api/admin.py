from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas import membership as schemas
from app.crud import membership as crud
from app.schemas import user_membership as um_schemas
from app.schemas.feature import FeatureCreate, FeatureOut
from app.crud import user_membership as um_crud
from app.crud.feature import create_feature
from app.models.user_membership import UserMembership
from app.models.feature import Feature
import uuid

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



# @router.post("/features", response_model=FeatureOut)
# def create_new_feature(data: FeatureCreate, db: Session = Depends(get_db)):
#    new_feature = Feature(
#        id=str(uuid.uuid4()),
#        name=feature.name,
#        description=feature.description
#    )
#    db.add(new_feature)
#    db.commit()
#    db.refresh(new_feature)
#    return {"id": new_feature.id, "name": new_feature.name, "description": new_feature.description}



@router.post("/features")
def create_feature(
    feature: FeatureCreate,
    db: Session = Depends(get_db)
):
    new_feature = Feature(
        id=str(uuid.uuid4()),
        name=feature.name,
        description=feature.description
    )
    db.add(new_feature)
    db.commit()
    db.refresh(new_feature)
    return new_feature

@router.post("/assign", response_model=um_schemas.UserMembershipOut)
def assign_membership(data: um_schemas.UserMembershipAssignRequest, db: Session = Depends(get_db)):
    return um_crud.assign_membership(db, data)


@router.get("/user/debug")
def debug_memberships(db: Session = Depends(get_db)):
    return db.query(UserMembership).all()

