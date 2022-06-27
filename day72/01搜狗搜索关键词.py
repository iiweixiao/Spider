import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


url = 'https://www.sogou.com/web'
kw = input('input a keyword:')
param = {
    'query': kw
}

resp = requests.get(url=url, params=param, headers=headers)
html = resp.text

filename = kw + '.html'
with open(filename, 'w', encoding='utf8') as f:
    f.write(html)

print('finished!')