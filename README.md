
---

## Ringle AI 튜터 과제 - Backend API 구현 (진행중)

### 📌 프로젝트 소개

본 과제는 Ringle의 AI 튜터 서비스를 위한 **풀스택 구현 과제**입니다. 현재까지 **FastAPI 기반의 백엔드 API**를 우선적으로 구축하였으며, **프론트엔드는 미착수 상태**입니다. 배포는 아직 진행되지 않았으며, 로컬 개발 환경에서 API를 테스트하고 있습니다.

### 📅 현재 진행 상황

| 항목                   | 상태    | 설명                                      |
| -------------------- | ----- | --------------------------------------- |
| `/admin/memberships` | ✅ 완료  | 멤버십 생성 및 기능 포함                          |
| `/admin/assign`      | ✅ 완료  | 특정 유저에게 멤버십 할당                          |
| `/user/membership`   | ✅ 완료  | 유저의 현재 멤버십 및 사용 가능한 기능 확인 가능            |
| `/user/use-feature`  | ✅ 완료  | 유저의 기능 사용 요청 처리 가능 (잔여 횟수 차감 포함)        |
| `/admin/features`    | ✅ 완료  | 기능(feature) 등록 API 구현 완료                |
| `/chat`              | ⏳ 진행중 | GPT 연동 API / 테스트 예정                     |
| `/mock/payment`      | ⏳ 진행중 | 결제 성공 시 멤버십 자동 부여 / 로직 설계 중             |
| 데이터베이스               | ✅ 완료  | PostgreSQL 기반 ORM 모델 구축 및 관계 정리 완료      |
| 배포                   | ❌ 미진행 | 현재 로컬 환경에서만 테스트 중이며 Docker-Compose 사용 중 |
| 프론트엔드 (React 기반)     | ❌ 미착수 | 이후 단계에서 홈 / 대화 / 결제 화면 등 구성 예정          |

---

## 🔧 사용 기술

* **Backend**: FastAPI, PostgreSQL, SQLAlchemy, Alembic
* **Infra**: Docker, Docker Compose
* **Etc**: .env 환경 변수 관리, Curl 기반 테스트, OpenAI API 예정

---

## 🧪 주요 API 테스트 예시

### 멤버십 생성

```bash
curl -X POST http://localhost:8000/admin/memberships \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Basic Plan",
    "duration_days": 30,
    "features": [
      { "feature_name": "chat", "limit_count": 10 },
      { "feature_name": "analysis", "limit_count": 5 }
    ]
  }'
```

### 유저에게 멤버십 할당

```bash
curl -X POST http://localhost:8000/admin/assign \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "test_user_2",
    "membership_id": "12a0fee3-524d-4665-85de-412212ed0c28"
  }'
```

### 유저 멤버십 조회

```bash
curl "http://localhost:8000/user/membership?user_id=test_user_2"
```

### 기능 사용 요청

```bash
curl -X POST http://localhost:8000/user/use-feature \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "test_user_2",
    "feature_name": "chat"
  }'
```

---

## 🧩 향후 계획

* `/chat`: GPT API 연동 로직 및 응답 처리
* `/mock/payment`: 결제 모의 처리 후 멤버십 자동 부여
* 프론트엔드 구현 (React + Web Speech API + Waveform 애니메이션)
* 전체 배포 자동화 구성 (Docker + GitHub Actions + AWS 예정)

---
