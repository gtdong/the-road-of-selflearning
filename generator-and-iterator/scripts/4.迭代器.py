'''
ls = [3, 1, 5, 2, 4]

# 通过索引循环取值
count = 0
while count < len(ls):
    print(ls[count], end=" ")
    count += 1
print()

# 寻求一种不依赖索引，且可以循环取值的方式
dic = {'a': 1, 'b': 2, 'c': 3}
print(dic)

# 通过__iter__()方法获取dic的一个不用依赖索引的取值容器
box = dic.__iter__()
print(box)
print(box.__next__())

box2 = ls.__iter__()
print(box2)
print(box2.__next__())

box3 = 'abc'.__iter__()
print(box3)
print(box3.__next__())

box4 = {'a', 'b', 'c'}.__iter__()
print(box4)
print(box4.__next__())

with open('1.txt', 'r', encoding='utf-8') as r:
    print(r)
    print(r.__next__())

dic_box = box
print(dic_box.__next__())


new_box = box.__iter__()
print(new_box.__next__())

print(dic)
dic_box = dic.__iter__()
'''

# 可迭代对象：可以被转化为不依赖索引取值的容器，这样的对象就叫做可迭代对象
#       -- 对象.__iter__() 来生成不依赖索引取值的容器
#       -- 结论：有__iter__()方法的对象都称之为 可迭代对象

# 迭代器对象：可以通过__next__()的方式进行取值的容器，且取一个少一个
#       -- 结论：有__next__()且可以通过__next__()进行取值的容器
#       -- 注意：迭代器对象自身也拥有__iter__(), 通过该方法返回的是迭代器对象自身

# 迭代器(for循环)：就是用来从可迭代对象中进行取值的循环方法 | 语法：for 变量 in 对象:
#       -- 1.通过对象.__iter__()获取其对应的迭代器对象
#           -- for可以操作迭代器对象及可迭代对象，统一写法，所以迭代器和可迭代对象都有__iter__()
#       -- 2.在内部通过迭代器对象的__next__()进行取值，将值赋值给 语法中的变量，取一个少一个
#       -- 3.当迭代器对象取完了，在内部自动捕获异常，并结束循环取值

dic1 = {'a': 1, 'b': 2, 'c': 3}  # dic是可迭代对象

# dic1_box = dic1.__iter__()  # 通过__iter__()得到的是迭代器对象
# # print(len(dic1_box))  # 迭代器对象没有len()方法
# while True:
#     try:
#         print(dic1_box.__next__())
#     except StopIteration:
#         # print('取完了')
#         break

for v in dic1:
    print(v)




