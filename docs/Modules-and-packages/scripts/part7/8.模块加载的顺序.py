"""
# 内置 | 自定义 模块
import time
print(time)


import my_time
print(my_time.num)


# time.sleep(7)
from time import sleep
sleep(7)

from my_time import num
print(num)
"""
# 模块的加载顺序:
# 内存 > 内置 > sys.path的遍历顺序

import json
print(json)

import time
print(time)


