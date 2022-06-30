import requests
import json


url = 'https://api.codelife.cc/api/top/list'
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'referer': 'https://go.itab.link/',
    'signaturekey': 'U2FsdGVkX1/rN/AZrL38LLGBt6iP85IQ5Ilk0QXls4A='
}
data = {
    id: "KqndgxeLl9"
}
resp = requests.post(url, data=data, headers=headers)

json_data = resp.json()
print(json_data)