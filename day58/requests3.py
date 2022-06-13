import requests

url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
}
# 重新封装参数
param = {
    'type': '5',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}

res = requests.get(url, headers=headers, params=param)
print(res.request.url)
print(res.text)
res.close()
