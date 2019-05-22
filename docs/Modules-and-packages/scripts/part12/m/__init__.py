# from m import m1

import m.m1 as m1

# 以上操作通过包名往下找,都成立,不管包在哪,但包名一旦被修改,
# __init__中依赖包名管理的名字都需要改变

# 包内的相对导入语法

from . import m1

from .mm.m2 import yyy

import time