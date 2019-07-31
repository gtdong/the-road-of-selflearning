# 同一个进程下多个线程数据是共享
from threading import Thread,active_count
import os
import time

money = 10

def task():
    global money
    money = 0
    print(os.getpid())
    time.sleep(1)

t = Thread(target=task)
t.start()
# print(money)
t.join()

print(active_count())  # 统计当前进程下 存活的线程数
print(os.getpid())
print('主')

"""
主线程一定要等待所有子线程的结束才会结束
因为主线程一旦结束意味着整个进程的结束,那么会造成子线程无法正常运行
"""
