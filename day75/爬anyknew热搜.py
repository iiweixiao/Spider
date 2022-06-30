import requests
import json


# weibo热搜
url = 'https://www.anyknew.com/api/v1/sites/weibo'

# 知乎热搜
# url = 'https://www.anyknew.com/api/v1/sites/zhihu'

resp = requests.get(url)
json_data = resp.json()


items_list = json_data['data']['site']['subs'][0]['items']
for index, item_dict in enumerate(items_list):
    iid = item_dict['iid']
    title = item_dict['title']
    # href = f'https://s.weibo.com/weibo?q={title}&Refer=top'
    href = f'https://www.anyknew.com/go/{iid}'
    # print(title, href)
    print(index+1, title, href)