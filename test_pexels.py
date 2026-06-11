import os
import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.environ.get("PEXELS_API_KEY")

if not KEY:
    print("[오류] .env에서 PEXELS_API_KEY를 못 찾았어요.")
    raise SystemExit

# 테스트 검색어 (나중엔 주제에 맞춰 자동으로 바뀜)
QUERY = "stock market finance"

url = "https://api.pexels.com/v1/search"
headers = {"Authorization": KEY}
params = {"query": QUERY, "per_page": 5, "orientation": "portrait"}

print(f"Pexels에서 '{QUERY}' 사진 검색 중...")
res = requests.get(url, headers=headers, params=params, timeout=30)

print("응답 코드:", res.status_code)

if res.status_code != 200:
    print("[실패] 응답 내용:", res.text[:300])
    raise SystemExit

data = res.json()
photos = data.get("photos", [])
print(f"찾은 사진 수: {len(photos)}장\n")

for i, p in enumerate(photos, 1):
    print(f"{i}. 작가: {p['photographer']}")
    print(f"   사진 URL: {p['src']['large']}")
    print()

print("done!")
