import requests

key = '苹果'
url = f'https://www.sogou.com/sogou?interation=1728053249&query={key}&'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
}

resp = requests.get(url, headers=headers)
print(resp.text)
