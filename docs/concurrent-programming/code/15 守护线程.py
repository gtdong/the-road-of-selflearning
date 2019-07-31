from threading import Thread,current_thread
import time

def task():
    print('%s is running'%current_thread().name)
    time.sleep(3)
    print('%s is end'%current_thread().name)

t = Thread(target=task)
t1 = Thread(target=task)
t.daemon = True
t.start()
t1.start()
print('主')
"""
同一个进程下
    主线程会等待所有非守护线程的结束才会结束 
"""


from threading import Thread
from multiprocessing import Process
import time
def foo():
    print(123)
    time.sleep(3)
    print("end123")
def bar():
    print(456)
    time.sleep(1)
    print("end456")
if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)
    t1.daemon=True
    t1.start()
    t2.start()
    print("main-------")