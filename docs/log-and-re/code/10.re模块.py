import re

r1 = re.findall(r'1', '123abc123')
print(r1)

r2 = re.findall(r'a', '123abc123ABC', flags=re.I)
print(r2)

# 1.将 r'\d' 丢给_compile得到可以匹配数字的 正则对象
# 2.正则对象.findall('目标字符串')
r3 = re.findall(r'\d', '123abc123')
print(r3)


re_obj = re.compile(r'\d')  # 将 r'\d' 丢给_compile得到可以匹配数字的 正则对象
r4 = re_obj.findall('123abc123')  # 正则对象.findall('目标字符串')
print(r4)




