"""
队列:FIFO 先进
"""
# from multiprocessing import Queue
# q = Queue(5)  # 生成一个队列对象  括号内可以通过参数指定队列最多容纳的元素个数
# q.put(1)  # 往队列中添加数据
# q.put(2)  # 往队列中添加数据
# q.put(3)  # 往队列中添加数据
# # print(q.full())
# q.put(4)  # 往队列中添加数据
# q.put(5)  # 往队列中添加数据
# print(q.full())  # 判断队列是否为空
# q.put(6)  # 如果超出队列最大值 会阻塞
# print(q.get())  # 获取队列中的元素
# print(q.get())  # 获取队列中的元素
# print(q.get())  # 获取队列中的元素
# print(q.get())  # 获取队列中的元素
# print(q.get())  # 获取队列中的元素
# print(q.get())  # 当队列中没有数据的时候 再取 会阻塞 直到拿到值
# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get_nowait())  # 当队列里面没有数据的时候 直接报错

"""
上述的full(),get_nowait()在多进程的情况下 不适用 无法给真正的答案
"""



# IPC机制   进程间通信
from multiprocessing import Process,Queue
# 队列 = 管道 + 锁


# def producer(q):
#     q.put('1')
#     q.put('hello world!')
#     q.put('hello world!')
#     q.put('hello world!')
#
# def consumer(q):
#     print(q.get())
#
# if __name__ == '__main__':
#     q = Queue(-1)
#     p = Process(target=producer,args=(q,))
#     c = Process(target=consumer,args=(q,))
#     p.start()
#     c.start()












