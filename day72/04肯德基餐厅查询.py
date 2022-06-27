import requests
import json

# keyword = input('input your city:')
keyword = '南京'
url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

post_data = {
    "cname": '',
    "pid": '',
    "keyword": keyword,
    "pageIndex": 1,
    "pageSize": 10
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

list_data = []
flag = True
while flag:
    resp = requests.post(url=url, data=post_data, headers=headers)
    text = resp.text
    table1 = json.loads(text)['Table1']
    if table1:
        list_data.append(table1)
        post_data['pageIndex'] += 1
    else:
        flag = False

print(list_data)

with open('KFC.json', 'w') as f:
    json.dump(list_data, fp=f, ensure_ascii=False)
