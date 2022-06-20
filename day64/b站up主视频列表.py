import requests
from datetime import datetime
from day65 import 发邮件

# mid为up主id号
mid = '927587'  # 木鱼水心id
mid = '550438936'
# mid = '37974444'
search = '水浒'  # 搜索内容或主题，空值就搜索所有内容
search = ''  # 搜索内容或主题，空值就搜索所有内容

flag = True
pn = 1  # 第一页
index = 1  # 视频排序（最新的为1）
content = ''
while flag:
    url = f'https://api.bilibili.com/x/space/arc/search?mid={mid}&ps=30&tid=0&pn={pn}&keyword=&order=pubdate&jsonp=jsonp'
    resp = requests.get(url)
    dic = resp.json()
    lst = dic['data']['list']['vlist']
    if lst == []:
        flag = False
    else:
        for i in lst:
            if search in i['title']:
                sub_url = 'https://www.bilibili.com/video/' + i['bvid']
                created = datetime.fromtimestamp(i['created'])  # 时间戳转日期 参考 https://zhuanlan.zhihu.com/p/337296461
                print(index, i['title'], created, i['length'], sub_url)  # 序号，标题，创建时间，总时常，视频地址
                content += f"{index} <a href='{sub_url}'>{i['title']}</a> {created} {i['length']} <br>"
                index += 1
        pn += 1
# 发邮件.send_email("813703110@qq.com", content, 'up主视频列表')
发邮件.send_email("weixiaot2021@icloud.com", content, 'up主视频列表')
