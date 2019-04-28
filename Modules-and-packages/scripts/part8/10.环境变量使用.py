import m1
print(m1)

# import sys
# sys.path.append(r'D:\python周末四期\week6_0427\代码\part8\a')
#
# import m2
# print(m2)
#
# sys.path.append(r'D:\python周末四期\week6_0427\代码\part8\b\c')
# import m3
# print(m3)

import a.m2
print(a.m2)
import a.m2 as m2
print(m2)
from a import m2
print(m2)

from b.c import m3
print(m3)

import sys
# 开发项目时,如何处理环境变量: 一定要将项目根目录添加至环境变量, 所有的导包从项目根目录开始
# print(__file__)
# print(sys.path)
from part7.aa.bb import cc
print(cc)