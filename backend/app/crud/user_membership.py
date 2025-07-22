# crud/user_membership.py
from sqlalchemy.orm import Session
from app.models.user_membership import UserMembership
from app.models.membership import Membership, MembershipFeature
from app.models.feature import Feature
from app.models.usage_history import UsageHistory
from app.schemas.user_membership import UserMembershipStatusOut, FeatureStatus, UserMembershipAssignRequest

def get_user_membership_status(db: Session, user_id: str) -> UserMembershipStatusOut:
    assignment = (
        db.query(UserMembership)
        .join(Membership, UserMembership.membership_id == Membership.id)
        .filter(UserMembership.user_id == user_id)
        .first()
    )

    if not assignment:
        raise ValueError("No membership assigned")

    features = (
        db.query(MembershipFeature, Feature)
        .join(Feature, MembershipFeature.feature_name == Feature.name)
        .filter(MembershipFeature.membership_id == assignment.membership_id)
        .all()
    )

    feature_statuses = []
    for mf, feature in features:
        used_count = (
            db.query(UsageHistory)
            .filter(
                UsageHistory.user_id == user_id,
                UsageHistory.feature_name == mf.feature_name
            )
            .count()
        )

        remaining_count = max(0, mf.limit_count - used_count)

        feature_statuses.append(FeatureStatus(
            feature_name=feature.name,
            used_count=used_count,
            remaining_count=remaining_count
        ))

    return UserMembershipStatusOut(
        membership_name=assignment.membership.name,
        start_date=assignment.start_date,
        end_date=assignment.end_date,
        features=feature_statuses
    )



from datetime import datetime, timedelta

def assign_membership(db: Session, data: UserMembershipAssignRequest):
    new_um = UserMembership(
        user_id=data.user_id,
        membership_id=data.membership_id,
        start_date=datetime.utcnow(),
        end_date=datetime.utcnow() + timedelta(days=30)
    )
    db.add(new_um)
    db.commit()
    db.refresh(new_um)
    return new_um

