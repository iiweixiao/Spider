import requests
from lxml import etree

url = 'https://sc.chinaz.com/jianli/free.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

}

def downloads(url):
    """ 江苏电信下载地址 """
    resp1 = requests.get(url=url, headers=headers)
    html1 = etree.HTML(resp1.text)
    down_link = html1.xpath('//*[@id="down"]/div[2]/ul/li[4]/a/@href')[0]
    print(down_link)
    return


resp = requests.get(url=url, headers=headers)
html = etree.HTML(resp.text)
divs = html.xpath('//*[@id="container"]/div')
for div in divs:
    href = div.xpath('./a/@href')[0]
    href = 'https:' + href
    downloads(href)




