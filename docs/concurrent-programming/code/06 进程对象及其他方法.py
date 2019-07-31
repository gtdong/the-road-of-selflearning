from multiprocessing import Process,current_process
import time
import os

def task():
    # print('%s is running'%current_process().pid)  # 查看当前进程的id号
    # print('%s is running'%os.getpid())  # 查看当前进程的id号
    print('%s is running'%os.getppid())  # 查看当前进程的父进程的id号
    # print('%s is running'%Process().pid)  # 查看当前进程的id号
    time.sleep(3)
    # print('%s is end'%current_process().pid)
    print('%s is end'%os.getpid())


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    print(p.name)
    p.terminate()  # 杀死子进程
    time.sleep(0.1)
    print(p.is_alive())  # 判断当前子进程是否存活
    # print('主:%s'%current_process().pid)
    # print('主:%s'%os.getpid())
    print('主:%s'%os.getppid())
    print(current_process().name)

