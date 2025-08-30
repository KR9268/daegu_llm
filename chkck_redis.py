from langchain_community.chat_message_histories import RedisChatMessageHistory
from dotenv import load_dotenv
import os

# dotenv 로 key 불러오기
load_dotenv()


# Redis 서버의 URL을 지정합니다.
REDISPW = os.getenv("REDISPW")
GCP_ENGINE_IP = os.getenv("GCP_ENGINE_IP")
# REDIS_URL = "redis://default:jon123@localhost:6379/0"
REDIS_URL = f"redis://default:{REDISPW}@{GCP_ENGINE_IP}:6379/0"

history = RedisChatMessageHistory(
    session_id="ssac0828",
    url=REDIS_URL
)

print(history.messages)