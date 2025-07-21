from sqlalchemy.orm import Session
from app.models import membership as models
from app.schemas import membership as schemas

def create_membership(db: Session, data: schemas.MembershipCreate):
    new_membership = models.Membership(
        name=data.name,
        duration_days=data.duration_days
    )
    db.add(new_membership)
    db.flush()  # ID를 먼저 얻기 위해

    for feature in data.features:
        db.add(models.MembershipFeature(
            membership_id=new_membership.id,
            feature_name=feature.feature_name,
            limit_count=feature.limit_count
        ))

    db.commit()
    db.refresh(new_membership)
    return new_membership

def get_memberships(db: Session):
    return db.query(models.Membership).all()

