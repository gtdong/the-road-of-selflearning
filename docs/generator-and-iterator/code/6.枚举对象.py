ls = [3, 1, 2, 5, 4]
# for v in ls:
#     print(v)

# count = 0
# while count < len(ls):
#     print(str(count + 1) + '次循环：' + str(ls[count]))
#     count += 1

# 枚举对象：为迭代器对象产生迭代索引
print(list(enumerate(ls)))
for i, v in enumerate(ls):
    print(str(i + 1) + '次循环：' + str(v))

dic = {'a': 100, 'b': 200}
print(list(enumerate(dic)))

