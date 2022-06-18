import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

web = Chrome(options=opt)
web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
sel = Select(web.find_element(by=By.XPATH, value='//*[@id="OptionDate"]'))
with open('艺恩电影排行.txt', 'w') as f:
    for i in range(len(sel.options)):
        sel.select_by_index(i)
        time.sleep(2)
        table = web.find_element(by=By.XPATH, value='//*[@id="TableList"]/table')
        f.writelines(table.text)
        f.writelines('\n==============\n')
        print('完成一页', i)

    # 打印时时渲染源码
time.sleep(3)
print(web.page_source)
