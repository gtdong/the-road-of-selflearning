"""
创建进程
    1.双击
    2.代码创建

进程是资源单位，进程之间数据隔离
同一份程序也可以有多个进程
"""
# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(3)
#     print('%s is end'%name)
#
#
# # windows操作中创建的方式 会将以模块导入的方式从头到尾执行当前文件
# # linux中 是直接当前文件的代码拷贝一份(fork)
# # p = Process(target=task,args=('jason',))  # 函数名加括号优先级最高
# # p.start()  # 告诉操作系统帮你创建一个进程:1.申请内存空间  2.执行当前文件中的代码 将产生的名字全部丢到新申请的名称空间中
# # print('主')
# if __name__ == '__main__':  # 双下name
#     p = Process(target=task,args=('jason',))  # 函数名加括号优先级最高
#     p.start()  # 告诉操作系统帮你创建一个进程:1.申请内存空间  2.执行当前文件中的代码 将产生的名字全部丢到新申请的名称空间中
#     print('主')




# @wrapper  # index = wrapper(index)
# def index():
#     pass
#
# def outter(a):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             return func(*args,**kwargs)
#         return inner
#     return wrapper
#
# @outter('jason')  # @wrapper
# def login():
#     ...



# 创建进程的第二种方式
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):  # 第二种方式里面的run就类似于第一种方式里面的task
        print('%s is running'%self.name)
        time.sleep(1)
        print('%s is end'%self.name)
if __name__ == '__main__':
    p = MyProcess('jason')
    p.start()
    print('主')






