import requests
from bs4 import BeautifulSoup


url = 'https://news.163.com/domestic/'
res = requests.get(url)

page = BeautifulSoup(res.text, 'html.parser')
data1 = page.find('div', attrs={'class': 'hidden'})
a = data1.findAll('a')
with open('网易新闻.txt', 'w') as f:
    for i in a:
        if '书记' in i.text:
            s = i.text + '\n' + i.get('href') + '\n' + '------' + '\n'
            print(i.text, '\n', i.get('href'))
            f.writelines(s)