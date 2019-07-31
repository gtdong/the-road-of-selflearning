# 列表推导式
# 产生1~10之间的偶数list => [2, 4, 6, 8, 10]
# ls = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         ls.append(i)
# print(ls)

# 语法：[结果 for 结果 in 可for循环操作的对象]
# 案例：[v for v in 'abc'] => ['a', 'b', 'c']

ls = [i for i in range(1, 11)]  # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ls)

# ls = ['' if i % 2 != 0 else i for i in range(1, 11)]
ls = [i for i in range(2, 11, 2)]  # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ls)


# 1~5之间的数用奇数偶数形参list => ['奇数', '偶数', '奇数', '偶数','奇数']
ls = ['奇数' if i % 2 != 0 else '偶数' for i in range(1, 6)]
print(ls)

# ls = ('奇数' if i % 2 != 0 else '偶数' for i in range(1, 6))
# print(tuple(ls))

# 字典推导式
# 语法：{k: v for k, v in 可for循环操作的对象(每一次循环的结果可以被解压为两个值)}
# 原数据: [('a', 1), ('b', 2)] => {'a': 1, 'b': 2}
source = [('a', 1), ('b', 2)]
# dic = {}
# for k, v in source:
#     dic[k] = v
# print(dic)

dic = {k: v for k, v in source}
print(dic)

dic = {i: 0 for i in 'abc'}
print(dic)

print({}.fromkeys('abc', 0))


