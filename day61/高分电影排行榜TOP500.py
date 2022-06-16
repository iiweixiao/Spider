from concurrent.futures import ThreadPoolExecutor

import requests
from lxml import etree

url = 'https://cn163.net/paihanbang/2/'
resp = requests.get(url)
print(type(resp.text))
html = etree.HTML(resp.text)
data = html.xpath('//*[@id="post-32261"]/div/div[1]')[0]
titles = data.xpath('./h3/text()')
# print(titles)


# 先放弃了，有点复杂
for i in range(len(titles)):
    print(titles[i])
    names = data.xpath(f'./h3[{i+1}]/following-sibling::*[1]/tbody/tr/td[1]/text()')
    for j in range(len(names)):
        print(names[i])

# def func(url):
#     resp = requests.get(url)
