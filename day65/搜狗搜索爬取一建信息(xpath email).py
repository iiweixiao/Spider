import requests
from lxml import etree
from utils import send_email

# key_words = ['一建', '一级建造师']
key_words = ['电动车', '新能源']
content = ''
index = 1

for key_word in key_words:

    # 搜狗搜索的资讯频道
    url = f'https://www.sogou.com/sogou?interation=1728053249&query={key_word}'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
    }
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)

    div_list = html.xpath('//*[@class="vrwrap"]')
    for i in div_list:
        title = i.xpath('./div/h3/a//text()')  # 拿到a标签及a标签内em标签的文字，['2022年报考','一建',',哪些地区需要社保?']
        title = ''.join(title)  # 合并文字
        href = i.xpath('./div/h3/a/@href')[0]
        href = 'https://www.sogou.com' + href
        source_from = i.xpath('./div/div//div/p/span[1]/text()')[0]
        created = i.xpath('./div/div//div/p/span[2]/text()')[0]
        print(title, source_from, created, href)
        content += f"{index} <a href='{href}'>{title}</a> <br>{source_from} {created} <br> <br>"
        index += 1

send_email.send_email('weixiaot2021@icloud.com', content, '电动车资讯_from搜狗搜索')
