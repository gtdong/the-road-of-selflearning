"""
什么是异常处理
    异常就是程序运行中出现的错误，如果改错误没有相应的处理机制
    那么这个错误就会抛出来，程序也会随之停止运行
为什么要有异常处理
    增强代码的健壮性
    try...except...
如何使用

"""
# print('start...')
# x = 1
# y = 2
# if
# print('end...')

# 异常三部分:
"""
1.报错类型
2.错误信息的值
3.错误的定位信息
"""

# 异常分类
"""
1.语法上的错误

2.逻辑上的错误
"""
# print('start ...')
# x = 1
# a
# print('end...')
# NameError

# print('start...')
# d = {'name':'jason'}
# d['password']
# print('end...')
# KeyError


# l = [12,3,4]
# l[123]
# IndexError
# try:
#     # d = {'name': 'jason'}
#     # d['password']
#     a = 1
#     x
#     l = [1,2,3,4]
#     l[123]
# except NameError:
#     print('变量未定义')
# except KeyError:
#     print('字典键不存在')
# except IndexError:
#     print('索引超出范围')




# 万能异常
# try:
#     # d = {'name': 'jason'}
#     # d['password']
#     # a = 1
#     # x
#     l = [1,2,3,4]
#     l[123]
# except Exception as e:  # 将错误信息的值赋值给变量a
#     print(e)

# 个人建议异常不要频繁使用 能尽量不用就不用   仅仅只加载会出现报错的几个行代码上下，try里面的代码越少越好


# try:
#     d = {'name': 'jason'}
#     d['password']
#     # a = 1
#     # x
#     # l = [1,2,3,4]
#     # l[123]
#     print('haha')
#     pass
# except Exception as e:
#     print(e)
# else:
#     print('当try里面的代码没有报错的情况下走else')
# finally:
#     print('无论前面有没有报错 我都会执行')


# raise 主动抛出异常
# class User:
#     def __init__(self,name):
#         self.__name = name
#     def set_info(self,val):
#         if not isinstance(val,str):
#             raise TypeError('name字段必须是str类型')
#         self.__name = val
# obj = User('jason')
# obj.set_info(123)


# l = [1,2,3,4]
# assert  len(l) < 0

# class MyError(BaseException):
#     def __init__(self,msg):
#         self.msg = msg
#
#     def __str__(self):
#         return '<%s>'%self.msg
# raise MyError('我自己定义了一个异常')





"""
try:
    可能报错的代码块
except 异常类型 as 异常信息:
    print(异常信息)
else:
    try监测的代码没有任何bug的情况下才会走else内部代码块
finally:
    无论是否出bug都会走finally内部的代码块



raise 主动抛出异常
    raise TypeError('异常信息')




assert 断言


自定义异常 继承BaseException  内部定义__str__来显示报错信息

"""







