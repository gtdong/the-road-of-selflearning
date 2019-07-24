"""
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple
native threads from executing Python bytecodes at once. This lock is necessary mainly
because CPython’s memory management is not thread-safe. (However, since the GIL
exists, other features have grown to depend on the guarantees that it enforces.)
"""
"""
1.GIL全局解释锁只在Cpython解释器上才有
2.GIL全局解释锁本质也是一把互斥锁
3.GIL全局解释锁用来锁主同一个进程下多个线程的运行
4.因为内存管理不是线程安全的

内存管理(垃圾回收机制)
    1.引用计数
    2.标记清除
    3.分代回收

1.cpython解释器下python的同一个进程下的多线程真的一点用没有吗？
你不能够直接下结论，应该分任务的类型来讨论
四个任务都是计算密集型的 10s
    多线程 40s+
    多进程 10s+
四个任务都是IO密集型的 10s
    多进程 
        1.申请内存空间
        2.执行代码
    多线程(优势的)

当你的任务是以计算为主那么你可以开多进程
当你的任务是以IO为主的那么你可以开多线程
        
"""
# 计算密集型  多进程
# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i
#
#
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count())  # 本机为6核
#     start=time.time()
#     for i in range(12):
#         p=Process(target=work) #耗时8.779496908187866s多
#         # p=Thread(target=work) #耗时44.838125467300415s多
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))




# IO密集型  多线程
# from multiprocessing import Process
# from threading import Thread
# import threading
# import os,time
# def work():
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     l=[]
#     print(os.cpu_count()) #本机为6核
#     start=time.time()
#     for i in range(400):
#         # p=Process(target=work) #耗时20.29075288772583s多,大部分时间耗费在创建进程上
#         p=Thread(target=work) #耗时 2.0506210327148438s多
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))