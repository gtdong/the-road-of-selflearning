
"""
# 锁：
1.将并发变成串行
2.降低了程序的运行效率但是提高数据的安全性
"""
# from multiprocessing import Process,Lock
from threading import Thread,Lock
import time
n = 100

def task(mutex):
    global n
    mutex.acquire()  # 抢锁
    temp = n
    time.sleep(0.1)
    n = temp - 1
    mutex.release()  # 释放锁

if __name__ == '__main__':
    mutex = Lock()
    t_list = []
    for i in range(100):
        t = Thread(target=task,args=(mutex,))
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    print(n)






















