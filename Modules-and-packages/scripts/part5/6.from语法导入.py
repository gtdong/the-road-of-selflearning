"""
# 在执行文件中能不能直接使用模块中的名字

# import m1
# import m1 as m
# print(m1.a)
# print(m1.b)
# print(m.a)
# print(m.b)

# 已经明确当前文件不去产生a,b,c三个名字，那a,b,c只有在m1中有，能不能直接用

from m1 import a
# 编译pyc => 执行模块产生名称空间存放名字 => 进入模块的名称空间取具体的名字
# 第三步：在执行文件起一个与模块中名字相同的变量指向那个名字的地址：a = m1.a
print(a)
import m1

a = 20
print(a)

print(m1.a)


# 起别名
from m1 import b as bbb  # bbb = m1.b
print(bbb)
"""

# 将模块中的名字一次性全部得到
from m1 import *  # a=m1.a b=m1.b c=m1.c
# print(a)
# print(b)
# print(c)
# print(x_)

# from 模块 import * 默认不导入_开头的名字
# print(_d)

# from m1 import b
# print(b)