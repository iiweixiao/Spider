import re

import requests

# 功能：查找多p视频的名称，总时长，分p列表与播放地址

# 思路：
# 1. 输入多p视频播放地址,通过正则解析出up主的mid号
# 2. 得到bvid
# 3. 列出up主所有视频的地址，如果bvid在地址中，则取到该视频总时长
# 4. 列出分p标题和播放地址
video_url = 'https://www.bilibili.com/video/BV1Lq4y127B2?vd_source=e7ed50c0d7d2387c7423c27fa17f7af5'
video_url = 'https://www.bilibili.com/video/BV1U94y1U7ZM?p=8&spm_id_from=pageDriver&vd_source=e7ed50c0d7d2387c7423c27fa17f7af5'
bvid = ''
if '?' in video_url:
    bvid = video_url.split('?')[0].rsplit('/', 1)[1]
else:
    bvid = video_url.rsplit('/', 1)[1]

# 总时长
resp1 = requests.get(video_url)
pattern = r'"owner":{"mid":(?P<mid>.*?),"name":'
obj = re.compile(pattern, re.S)
# print(resp1.text)
result = obj.finditer(resp1.text)
for it in result:
    mid = it.group('mid')
# 根据mid号，获取标题和总时长
flag = True
pn = 1  # 第一页
while flag:
    url2 = f'https://api.bilibili.com/x/space/arc/search?mid={mid}&ps=30&tid=0&pn={pn}&keyword=&order=pubdate&jsonp=jsonp'
    resp = requests.get(url2)
    dic = resp.json()
    lst = dic['data']['list']['vlist']
    if lst == []:
        flag = False
    else:
        for i in lst:
            if bvid == i['bvid']:
                print(i['title'], i['length']+'分钟')  # 序号，标题，创建时间，总时常，视频地址
        pn += 1


url = f'https://api.bilibili.com/x/player/pagelist?bvid={bvid}&jsonp=jsonp'  # 有多p
# url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV19F411V7X4&jsonp=jsonp'  # 只有1p
# 获取分p的名称和播放地址
resp = requests.get(url)
dic = resp.json()
lst = dic['data']
index = 1
if len(lst) == 1:
    print()
for i in lst:
    print(index, i['part'], f'https://www.bilibili.com/video/{bvid}?p={index}')
    index += 1


