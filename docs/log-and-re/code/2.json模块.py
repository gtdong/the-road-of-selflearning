
import json

# python对象 序列化 json字符串
data = None
res = json.dumps(data)
print(res)

# json字符串 反序列化 python对象
json_str = '3.14'
json_str = 'true'
json_str = 'null'
json_str = '{}'
json_str = '[]'
json_str = '1, null'  # 有误，两个根

json_str = "\"abc\""
json_str = '"abc"'
obj = json.loads(json_str)
print(obj, type(obj))


# 操作文件
# 序列化
obj = {'name': 'Owen', 'age': 17, 'gender': '男'}

with open('a.txt', 'w', encoding='utf-8') as wf:
    json.dump(obj, wf, ensure_ascii=False)
    # json.dump(obj, wf, ensure_ascii=False)
    # wf.write('123')
    # wf.write('456')

# 反序列化
with open('a.txt', 'r', encoding='utf-8') as rf:
    obj = json.load(rf)
    print(obj)

# 注：json模块的序列化与反序列化是一一对应关系

print(json.load(open('a.txt', 'r', encoding='utf-8')))