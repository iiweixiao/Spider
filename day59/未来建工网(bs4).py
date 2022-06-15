import requests
from bs4 import BeautifulSoup

url = 'https://www.jianzao.com/yijian/bm/'
resp = requests.get(url)

page = BeautifulSoup(resp.text, 'html.parser')

data = page.find('div', attrs={'class': 'tab1'})
news = data.findAll('a')
with open('一建信息.txt', 'w') as f:
    for i in news:
        news_url = url[0:len(url)-1] + i.get('href')
        print(i.text, news_url)
        s = i.text + '\n' + news_url + '\n' + '-------' + '\n'
        f.writelines(s)