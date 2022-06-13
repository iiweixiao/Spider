import re

s = '我的电话是17657482262，mary的电话是15811223344'

lst = re.findall(r'\d+', s)
print(lst)

it = re.finditer(r'\d+', s)
print(it)
for i in it:
    print(i.group())

s1 = re.search(r'\d+', s)
print(s1)
print(s1.group())

s2 = re.match(r'\d+', s)
# print(s2.group())


obj = re.compile(r'\d+')
s3 = obj.findall(s)
print(s3)

ss = """
<div class='jay'><span id='2'>周杰伦</span></div>
<div class='jj'><span id='2'>林俊杰</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tony'><span id='5'>胡说八道</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wao>.*?)</span></div>", re.S)  # re.S让.能匹配换行
result = obj.finditer(ss)
for it in result:
    print(it.group('id'), it.group('wao'))
