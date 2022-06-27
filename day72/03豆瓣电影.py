import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
param = {
    "type": 14,
    "interval_id": "100:90",
    "action": '',
    "start": 0,
    "limit": 20
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

resp = requests.get(url=url, params=param, headers=headers)
list_data = resp.json()

# 持久化
with open('豆瓣电影（音乐类型）.json', 'w') as f:
    json.dump(list_data, fp=f, ensure_ascii=False)

print('over')