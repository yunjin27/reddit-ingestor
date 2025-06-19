import os
from dotenv import load_dotenv
from pathlib import Path

# 루트 디렉토리 기준 .env 또는 .env.sample 로드
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / ".env"
if not dotenv_path.exists():
    dotenv_path = BASE_DIR / ".env.sample"
load_dotenv(dotenv_path=dotenv_path)

# Reddit API 설정
REDDIT_CONFIG = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "user_agent": os.getenv("REDDIT_USER_AGENT", "script:reddit-ingestor:v1.0 (by u/your_username)")
}

# Kafka 설정
KAFKA_CONFIG = {
    "bootstrap_servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS", "").split(","),
    "topic": os.getenv("KAFKA_TOPIC")
}

# 대상 서브레딧 목록 (쉼표 구분 후 공백 제거)
SUBREDDITS = [s.strip() for s in os.getenv("REDDIT_SUBREDDITS", "").split(",") if s.strip()]
