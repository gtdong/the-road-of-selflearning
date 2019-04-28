# 匿名函数：没有名字的函数
# 1.用lambda声明匿名函数
# 2.没有函数名，lambda与:之间一定是参数列表，参数列表省略()，且支持所有参数语法
# 3.匿名函数没有函数体，只有返回值，所有省略了return，且返回值只能有一个
#       -- (不能将多个返回值自动格式化为元组)

# def fn(x, y):
#     print(x)
#     print(y)
#     return x + y

# lambda x, y: (x + y, x - y)

# 应用场景
# 1.用一个变量接收，该变量就充当与函数的名字 - 不常见
# func = lambda x, y: (x + y, x - y)
# print(func(10, 20))

# 2.结合内置函数来使用
# print(max(10, 5, 3, 30, 20))
# print(max([10, 5, 3, 30, 20]))

def fn1(x):
    print(x)
    return x
max_num = max([10, 5, 3, 30, 20], key=fn1)
# max的工作原理
# 1.max要去遍历所有求大值的数据，这些一一被遍历出来的数要被依次传入key=fn的fn中
#       -- fn必须有参数，且只有一个参数，就是当前被遍历出来的被比较的数据
# 2.max再根据fn的返回值决定比较大小的依据
print('max_num: %s' % max_num)

dic = {
    'owen': (1, 88888),
    'egon': (2, 300000),
    'liuXX': (3, 99999)
}
def fn2(k):
    # return k  # 求名字最大
    # return dic[k][0]  # 求工号最大
    return dic[k][1]  # 求薪资最大
max_p = max(dic, key=fn2)
print(max_p)


# min函数的工作原理
# 1.min要去遍历所有求小值的数据，这些一一被遍历出来的数要被依次传入key=fn的fn中
#       -- fn必须有参数，且只有一个参数，就是当前被遍历出来的被比较的数据
# 2.min再根据fn的返回值决定比较大小的依据

dic = {
    'owen': (1, 88888),
    'egon': (2, 300000),
    'liuXX': (3, 99999)
}
res = min(dic, key=lambda x: dic[x][1])
print(res)

