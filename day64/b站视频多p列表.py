import requests

bvid = 'BV17F411T7Ao'
url = f'https://api.bilibili.com/x/player/pagelist?bvid={bvid}&jsonp=jsonp'  # 有多p
# url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV19F411V7X4&jsonp=jsonp'  # 只有1p

resp = requests.get(url)
dic = resp.json()
lst = dic['data']
index = 1
if len(lst) == 1:
    print()
for i in lst:
    print(index, i['part'], f'https://www.bilibili.com/video/{bvid}?p={index}')
    index += 1
