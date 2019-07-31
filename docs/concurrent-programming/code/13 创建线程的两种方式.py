# from threading import Thread
# import time
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(3)
#     print('%s is end'%name)
#
# t = Thread(target=task,args=('jason',))
# t.start()  # 创建线程  这句话一运行完 线程几乎就已经创建完毕了
# print('主')


# 第二种方式
from threading import Thread
import time
class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print('%s is running'%self.name)
        time.sleep(3)
        print('%s is end'%self.name)
t = MyThread('jason')
t.start()
print('主')