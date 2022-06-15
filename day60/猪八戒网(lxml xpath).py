import requests
from lxml import etree

# url = 'https://zp.zbj.com/search/all?kw&po=100109'
url = 'https://zp.zbj.com/search/all?kw&po=100101'
resp = requests.get(url)
# print(resp.text)
html = etree.HTML(resp.text)  # 'lxml.etree._Element'类型
# data = etree.tostring(html, encoding='utf-8').decode()  # 'str' 类型
divs = html.xpath('//*[@id="__layout"]/div/div[5]/div/div[2]/section[1]/ul/li')
for div in divs:
    title = div.xpath('./div//div[@class="title"]/text()')[0]
    location = div.xpath('./div//div[@class="region diandiandian"]/text()')[0]
    salary = div.xpath('./div//div[@class="salary"]/text()')[0]
    work_age = div.xpath('./div//div[@class="more-box"]/div[2]/text()')[0]
    degree = div.xpath('./div//div[@class="more-box"]/div[4]/text()')[0]
    print(title, location, salary, work_age, degree)

