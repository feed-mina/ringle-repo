from sqlalchemy.orm import Session
from app.models.user_membership import UserMembership
from app.models.membership import Membership
from app.schemas.user_membership import UserMembershipAssignRequest
from datetime import datetime, timedelta
import uuid

def assign_membership(db: Session, data: UserMembershipAssignRequest):
    membership = db.query(Membership).filter(Membership.id == str(data.membership_id)).first()
    if not membership:
        raise ValueError("Membership not found")

    now = datetime.utcnow()
    new_assignment = UserMembership(
        id=str(uuid.uuid4()),
        user_id=data.user_id,
        membership_id=str(data.membership_id),
        start_date=now,
        end_date=now + timedelta(days=membership.duration_days)
    )

    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return new_assignment

