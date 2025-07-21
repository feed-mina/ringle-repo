echo "⏳ Wait for PostgreSQL to be ready..."
sleep 5

echo "⏰ 현재 시간 확인 중..."
PGPASSWORD=postgres1234 psql -h db -U postgres -d ringle -c "SELECT NOW();"

echo "��� 테이블 생성 중..."
PGPASSWORD=postgres1234 psql -h db -U postgres -d ringle <<EOF
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS memberships (
  id UUID PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  duration_days INT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS membership_features (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  membership_id UUID REFERENCES memberships(id),
  feature_name VARCHAR(50),
  limit_count INT
);
EOF

echo "��� 데이터 삽입 시작..."
PGPASSWORD=postgres1234 psql -h db -U postgres -d ringle <<EOF
INSERT INTO memberships (id, name, duration_days, created_at)
VALUES
  ('00000000-0000-0000-0000-000000000001', '프리미엄', 60, NOW()),
  ('00000000-0000-0000-0000-000000000002', '베이직', 30, NOW());

INSERT INTO membership_features (id, membership_id, feature_name, limit_count)
VALUES
  (gen_random_uuid(), '00000000-0000-0000-0000-000000000001', 'chat', 20),
  (gen_random_uuid(), '00000000-0000-0000-0000-000000000001', 'analysis', 5),
  (gen_random_uuid(), '00000000-0000-0000-0000-000000000002', 'chat', 10),
  (gen_random_uuid(), '00000000-0000-0000-0000-000000000002', 'analysis', 2);
EOF

