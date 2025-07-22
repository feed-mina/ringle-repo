# app/crud/use_feature.py

from sqlalchemy.orm import Session
from app.models.user_membership import UserMembership
from app.models.membership import MembershipFeature
from app.models.usage_history import UsageHistory
from datetime import datetime

def use_feature(db: Session, user_id: str, feature_name: str):
    now = datetime.utcnow()

    # 1. 유저의 활성 멤버십 가져오기
    membership = (
        db.query(UserMembership)
        .filter(UserMembership.user_id == user_id)
        .filter(UserMembership.end_date >= now)
        .order_by(UserMembership.start_date.desc())
        .first()
    )
    if not membership:
        return False, "멤버십이 없습니다", None

    # 2. 멤버십의 기능 제한 정보 조회
    feature = (
        db.query(MembershipFeature)
        .filter(MembershipFeature.membership_id == membership.membership_id)
        .filter(MembershipFeature.feature_name == feature_name)
        .first()
    )
    if not feature:
        return False, "해당 기능을 사용할 수 없습니다", None

    # 3. 사용 기록 조회
    used_count = (
        db.query(UsageHistory)
        .filter(UsageHistory.user_id == user_id)
        .filter(UsageHistory.feature_name == feature_name)
        .count()
    )

    if feature.limit_count != -1 and used_count >= feature.limit_count:
        return False, "사용 가능 횟수를 초과했습니다", 0

    # 4. 기록 삽입
    usage = UsageHistory(
        user_id=user_id,
        feature_name=feature_name,
        used_at=now
    )
    db.add(usage)
    db.commit()

    remaining = (
        None if feature.limit_count == -1
        else feature.limit_count - used_count - 1
    )

    return True, "사용 완료", remaining

