import requests

query = input('输入你要翻译的内容：')

url = 'https://fanyi.baidu.com/sug'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
}
data = {
    'kw': query
}

res = requests.post(url, headers=headers, data=data)
print(res.json())
res.close()
