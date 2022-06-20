#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 需求：爬取搜狗首页的页面数据

# noinspection PyUnresolvedReferences
import requests

if __name__ == '__main__':
    # UA伪装:将访问对象伪装为浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    # 爬虫主体
    url = 'https://www.sogou.com/web'
    # 1. 处理url携带的参数：封装到字典中
    keyword = input('搜狗搜索：')
    param = {
        'query': keyword
    }

    # 2. 获取数据
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text

    # 3. 数据持久化
    filename = keyword + '.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('爬取完毕！')