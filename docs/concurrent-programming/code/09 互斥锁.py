from multiprocessing import Process,Lock
import json
import time
import random

"""
多个进程同一时间操作同一份数据的时候会造成数据的错乱
如何解决这一现象?
    锁:互斥锁
    多个人抢一个厕所的药匙
    
互斥锁特点
    1.牺牲了程序的效率但是保证了数据的安全

ps:你自己千万不要随意处理锁的问题,  处理不得当会造成死锁现象

互斥锁应该在主进程中产生 交给子进程去使用

锁会将并发变成串行
"""

"""
1.查票
2.买票
    1.查票
    2.买票
"""


def check(name):
    with open('ticket',encoding='utf-8') as f:
        data = json.load(f)
    print('当前余票:%s'%data.get("ticket"))

def buy(name):
    with open('ticket',encoding='utf-8') as f:
        data = json.load(f)
    # 模拟网络延迟
    time.sleep(random.randint(1,3))
    if data.get('ticket') > 0:
        data['ticket'] -= 1
        with open('ticket','w',encoding='utf-8') as f:
            json.dump(data,f)
        print('%s抢票成功'%name)
    else:
        print('没票了 回不了家了!')

def run(name,mutex):
    check(name)
    mutex.acquire()  # 抢锁
    buy(name)
    mutex.release()  # 释放锁

if __name__ == '__main__':
    mutex = Lock()  # 产生了一把
    for i in range(10):
        p = Process(target=run,args=('子进程:%s'%i,mutex))
        p.start()






# f = open('ticket',encoding='utf-8')
# print(json.load(f))
# f.close()

# d = {"name":"jason"}
# print(json.dumps(d))  # '{"name":"jason"}'
# print(d)