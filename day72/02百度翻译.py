import requests
import json

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

kw = input('input a word:')

data = {
    'kw': kw
}
resp = requests.post(url=url, data=data, headers=headers)
dic_obj = resp.json()


# 持久化
filename = kw + '.json'
with open(filename, 'w') as f:
    json.dump(dic_obj, fp=f, ensure_ascii=False)
print('over')
