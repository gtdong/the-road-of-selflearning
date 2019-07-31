"""
生产者消费者模型(celery消息队列)
    生产者:生产的数据(做包子的)
    消费者:处理数据的(吃包子的)
"""
from  multiprocessing import Process,Queue,JoinableQueue
import time
import random


def producer(name,food,q):
    for i in range(3):
        data = '%s生产了%s%s'%(name,food,i)
        time.sleep(random.randint(1,3))
        q.put(data)
        print(data)


def consumer(name,q):
    while True:
        data = q.get()
        if data == None:break
        time.sleep(random.randint(1,3))
        print('%s吃了%s'%(name,data))
        q.task_done()  # 已经从队里中拿到数据  并且处理完毕了

if __name__ == '__main__':
    q = JoinableQueue()
    p = Process(target=producer,args=('大厨jason','肉包子',q))
    p1 = Process(target=producer,args=('配菜owen','馒头',q))
    c = Process(target=consumer,args=('吃货egon',q))
    c1 = Process(target=consumer,args=('坑货尚老师',q))
    p.start()
    p1.start()
    c.daemon = True
    c1.daemon = True
    c.start()
    c1.start()

    p.join()
    p1.join()
    q.join()  # 等带队列中所有的数据都被取干净



