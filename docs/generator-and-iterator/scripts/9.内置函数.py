# print('123'.__len__())
# print(len('123'))


# 排序：sorted
dic = {
    'owen': (1, 88888),
    'egon': (2, 300000),
    'liuXX': (3, 99999)
}

# 总结：排序的可迭代对象，排序的规则，是否反转
res = sorted(dic, key=lambda k: dic[k][1], reverse=True)  # 按薪资排序的人名list
for k in res:
    print(k, dic[k][1])


# map：映射 - 格式化每一次的遍历结果
names = ['Owen', 'Egon', 'Liuxx']
def fn(x):
    # print(x)
    # 将所有名字全小写
    return x.lower()

res = map(fn, names)
print(list(res))


# ls = [88888, 300000, 99999]
# # 薪资加一元
# res = map(lambda x: x + 1, ls)
# print(list(res))

dic1 = {
    'owen': 88888,
    'egon': 300000,
    'liuXX': 99999
}
def fn1(x):
    dic1[x] += 1
    return 10000
# 总结：遍历第二个参数(可迭代对象)，将遍历的结果丢给第一个函数，
# 函数有一个参数，就是一一遍历的值
# map的作用(返回值)：在当前数据基础上改变值（可以任意修改）
res = map(fn1, dic1)
print(list(res))
print(dic1)


# 合并：reduce
from functools import reduce
# 求[1, 3, 4, 2, 10]所有元素的总和
res = reduce(lambda x, y: x + y, [1, 3, 4, 2, 10])
print(res)



# 已见过的
# 1.类型转换：int() tuple()
# 2.常规使用：print() input() len() next() iter() open() range() enumerate() id()
# 3.进制转换：bin() oct() hex() 将10进制转换为2 | 8 | 16进制
print(bin(10))  # 0b1010
print(oct(10))  # 0o12
print(hex(10))  # 0xa

# 3.运算：abs()
print(abs(-1))  # 绝对值
print(chr(9326))  # 将ASCII转换为字符
print(ord('①'))  # 逆运算
print(pow(2, 3))  # 2的3次方
print(pow(2, 3, 3))  # 2的3次方对3求余
print(sum([1, 2, 3]))  # 求和

# 4.反射：getattr() delattr() hasattr() setattr()

# 5.面向对象的相关方法：super() staticmethod() classmethod()
def fn():pass
print(callable(fn))  # 对象能不能被调用

# 6.原义字符串
print('a\nb')
s = ascii('a\nb')
print(s)
s = repr('a\nb')
print(s)
print(r'a\nb')

print(all([1, 0, 0]))
print(any([0, 0, 1]))

# compile() exec() eval()


