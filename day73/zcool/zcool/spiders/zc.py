import scrapy
from zcool.items import ZcoolItem  # 导入items.py中ZcoolItem类


count = 1  # 用于网站翻页计数

class ZcSpider(scrapy.Spider):
    name = 'zc'
    allowed_domains = ['www.zcool.com.cn']
    start_urls = ['http://www.zcool.com.cn/']

    def parse(self, response):
        global count
        count += 1

        div_list = response.xpath('//div[@class="sc-hKwDye jgyXZm workList"]/div')
        # print(len(divList))  # 测试用，显示40（对应40个封面）就说明上面xpath设置对了
        for div in div_list:
            try:
                img_link = div.xpath('./div[@class="cardImg"]//img/@src').extract_first()
                title = div.xpath('./section/div/span[1]/a/@title').extract_first()
                types = div.xpath('./section/span/@title').extract_first()
                visitor = div.xpath('./section/div[2]/div[1]/@title').extract_first()
                comment = div.xpath('./section/div[2]/div[2]/@title').extract_first()
                likes = div.xpath('./section/div[2]/div[3]/@title').extract_first()

                # 怎么理解下面 https://zhuanlan.zhihu.com/p/351093647#circle=on
                item = ZcoolItem(img_link=img_link, title=title, types=types, visitor=visitor, comment=comment,
                                 likes=likes)  # 类似字典，作用和说明中相同

                yield item
            except:
                print('e.....')

        next_url = f'https://www.zcool.com.cn/home?p={count}#tab_anchor'  # 下一页
        yield scrapy.Request(next_url)

    # 老师在爬取51job时用了回调函数callback
    # url = response.urljoin(next)
    # yield scrapy.Request(url=url, callback=self.parse)
