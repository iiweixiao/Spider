import json

# 将字典写入json文件
di = {'名字': '其他', 'age': 15}
with open("test.json", 'w', encoding='utf-8') as f:
    json.dump(di, f, ensure_ascii=False)

# 从json文件中读取数据
with open('test.json', 'r', encoding='utf-8') as f1:
    a = json.load(f1)
    print(a['age'])
    print(type(a))
di.update({'1': 2, '3': 4})
print(di)