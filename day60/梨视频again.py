import requests
from lxml import etree

def func(url):
    # 网页地址
    # url = 'https://www.pearvideo.com/video_1765343'
    contId = url.split('_')[1]

    # 视频真实下载地址
    # src = "https://video.pearvideo.com/mp4/short/20220614/cont-1765343-15895915-hd.mp4"

    # 通过开发工具找到视频api(非真实地址，需要观察，然后处理)
    # contId后的数字与网页地址中的数字一致
    # Request_URL = 'https://www.pearvideo.com/videoStatus.jsp?contId=1765343&mrd=0.3296261494517112'
    api = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.3296261494517112'

    # 有反爬，先试UA，再试防盗链
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Referer': f'https://www.pearvideo.com/video_{contId}'
    }
    resp = requests.get(api, headers=headers)
    dic = resp.json()

    # 查看json格式中视频地址，和真实视频下载地址比较，需要进行处理
    # srcUrl: "https://video.pearvideo.com/mp4/short/20220614/1655304165734-15895915-hd.mp4"
    srcUrl = dic['videoInfo']['videos']['srcUrl']
    systemTime = dic['systemTime']
    realUrl = srcUrl.replace(systemTime, f'cont-{contId}')

    # 测试，单个页面的视频地址抓去成功
    return realUrl


# 梨视频科技频道
channel_url = 'https://www.pearvideo.com/category_31'
resp1 = requests.get(channel_url)
html = etree.HTML(resp1.text)
# print(type(html))

titles = []
contIds = []
ul = html.xpath('//*[@id="listvideoListUl"]')  # 最新视频3个
for li in ul:
    titles = li.xpath('./li/div/a/div[2]/text()')  # 返回列表
    contIds = li.xpath('./li/div/a/@href')

ul = html.xpath('//*[@id="categoryList"]')  # 最热视频n个
for li in ul:
    titles.extend(li.xpath('./li/div/a/div[2]/text()'))  # 返回列表
    contIds.extend(li.xpath('./li/div/a/@href'))

def flag(l1, l2):
    flag = False
    for i in l1:
        if i in l2:
            return True
    if l1 == []:
        return True

for i in range(len(titles)):
    url = 'https://www.pearvideo.com/' + contIds[i]
    l1 = ['蔚来', '车']
    if flag(l1, titles[i]):
        print(titles[i], func(url))  #不带翻页，只能展示第一次加载的所有视频


