from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import membership as models
from app.models.user_membership import UserMembership
from app.models.usage_history import UsageHistory
from app.schemas.user_membership import UserMembershipStatusOut, FeatureStatus
from datetime import datetime

def get_user_membership_status(db: Session, user_id: str):
    now = datetime.utcnow()

    active_membership = db.query(UserMembership)\
        .filter(UserMembership.user_id == user_id)\
        .filter(UserMembership.end_date >= now)\
        .order_by(UserMembership.start_date.desc())\
        .first()

    if not active_membership:
        return None

    features = db.query(models.MembershipFeature).filter(
        models.MembershipFeature.membership_id == active_membership.membership_id
    ).all()

    usage = db.query(
        UsageHistory.feature_name,
        func.count(UsageHistory.id).label("used_count")
    ).filter(
        UsageHistory.user_id == user_id
    ).group_by(UsageHistory.feature_name).all()

    usage_dict = {row.feature_name: row.used_count for row in usage}

    feature_status = []
    for f in features:
        used = usage_dict.get(f.feature_name, 0)
        remaining = f.limit_count if f.limit_count == -1 else max(0, f.limit_count - used)
        feature_status.append(FeatureStatus(
            feature_name=f.feature_name,
            used_count=used,
            remaining_count=remaining
        ))

    return UserMembershipStatusOut(
        membership_name=active_membership.membership.name,
        start_date=active_membership.start_date,
        end_date=active_membership.end_date,
        features=feature_status
    )

