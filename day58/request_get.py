import requests

query = input('输入你要搜索的内容：')

url = f'https://www.sogou.com/web?query={query}'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
}



res = requests.get(url, headers=headers)
print(res)
print(res.text)
res.close()