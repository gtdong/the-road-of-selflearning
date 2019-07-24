"""
无论是多进程还是多线程 你都不应该无限制开下去
因为这样会造成硬件层面上的损坏 而一旦硬件损坏了 你的代码再牛逼也没有用武之地

原因
    为了保证计算机硬件能够正常运行

池:
    降低了程序的运行效率但是保证了计算机硬件安全
"""

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import time
import os

# pool = ThreadPoolExecutor(20)  # 不传参数默认是你当前计算机核数的五倍
pool = ProcessPoolExecutor(5)
# 会创建一个池子  里面固定已经产生了20个线程



def task(n):
    print(n,os.getpid())
    time.sleep(2)
    return n**2

def get_res(res,n):
    print('拿到了结果:%s'%res.result())

if __name__ == '__main__':
    for i in range(20):
        pool.submit(task,i).add_done_callback(get_res)  # 异步回调
        # print(res.result())  # 同步
























