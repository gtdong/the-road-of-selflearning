# num = int(input('num: '))

# 三元运算符（三目运算符）：就是简写if...else...结构
# if num > 10:
#     print('num值大于10')
# else:
#     print('num值不大于10')

# 语法：结果1 if 条件 else 结果2
# print('num值大于10') if num > 10 else print('num值不大于10')


# 案例：获得两个数中的大值 | 小者
n1 = int(input('n1: '))
n2 = int(input('n2: '))
res = n1 if n1 > n2 else n2
print(res)
res = n2 if n1 > n2 else n1
print(res)
