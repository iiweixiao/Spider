import requests
import re

main_url = 'https://www.dytt89.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
}

resp = requests.get(main_url, headers=headers)
resp.encoding = 'gb2312'
# print(resp.text)

obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(
    r'◎片　　名　(?P<movie_name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<movie_download_href>.*?)"',
    re.S)

# 得到<li>字符串
ul_string = obj1.finditer(resp.text)
for it in ul_string:
    ul = it.group('ul')

half_url = obj2.finditer(ul)
ul_list = []
for it in half_url:
    url = main_url + it.group('href').strip()
    ul_list.append(url)

for sub_url in ul_list:
    resp1 = requests.get(sub_url)
    resp1.encoding = 'gb2312'
    ss = resp1.text
    resp2 = obj3.finditer(ss)
    for itt in resp2:
        name = itt.group('movie_name')
        links = itt.group('movie_download_href')
        print('爬取完一条数据')
        with open('movie.txt', 'a') as f:
            f.writelines(name)
            f.writelines('\n')
            f.writelines(links)
            f.writelines('\n')
            f.writelines('------')
            f.writelines('\n')


