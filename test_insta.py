import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("IG_TOKEN")

if not TOKEN:
    print("[오류] .env에서 IG_TOKEN을 못 찾았어요.")
    raise SystemExit

print("토큰 길이:", len(TOKEN))
print("토큰 시작:", TOKEN[:6], "...\n")

# 1) 이 토큰이 어떤 인스타 계정인지 확인
url = "https://graph.instagram.com/me"
params = {"fields": "user_id,username,account_type", "access_token": TOKEN}

print("인스타 계정 정보 확인 중...")
res = requests.get(url, params=params, timeout=30)
print("응답 코드:", res.status_code, "\n")

if res.status_code == 200:
    data = res.json()
    print("=== 연결 성공! ===")
    print("  계정명(username):", data.get("username"))
    print("  계정 ID(user_id):", data.get("user_id"))
    print("  계정 종류:", data.get("account_type"))
    print("\n이 user_id를 .env에 저장하면 돼요!")
else:
    print("[실패] 응답 내용:")
    print(res.text[:500])
