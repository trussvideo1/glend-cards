import feedparser
from datetime import datetime, timedelta, timezone
import urllib.parse

# 구글 뉴스 RSS - 한국 경제 뉴스
QUERY = "경제 OR 금리 OR 증시 OR 부동산 when:1d"
url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(QUERY) + "&hl=ko&gl=KR&ceid=KR:ko"

print("구글 뉴스에서 최신 경제 뉴스를 가져올게요...\n")
feed = feedparser.parse(url)

print(f"총 {len(feed.entries)}개의 뉴스를 찾았어요!\n")
print("=== 최신 경제 뉴스 제목 (상위 15개) ===")
for i, entry in enumerate(feed.entries[:15], start=1):
    print(f"{i}. {entry.title}")
print("=====================================")
