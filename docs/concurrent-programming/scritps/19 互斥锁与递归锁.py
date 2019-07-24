from threading import Thread,Lock,RLock
import time

# mutexA=Lock()
# mutexB=Lock()
mutexB=mutexA=RLock()  # 递归锁
"""
递归锁自身有计数功能 他能够记住 被acquire了多少次
只有第一个抢到递归锁才能够连续的acquire连续的release
"""

class Mythead(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 抢到A锁' %self.name)
        mutexB.acquire()
        print('%s 抢到B锁' %self.name)
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 抢到了B锁' %self.name)
        time.sleep(2)
        mutexA.acquire()
        print('%s 抢到了A锁' %self.name)
        mutexA.release()
        mutexB.release()

if __name__ == '__main__':
    for i in range(100):
        t=Mythead()
        t.start()