# 并发编程

1.操作系统发展史

2.进程理论

3.创建进程的两种方式

4.join方法

5.进程之间数据互相隔离

6.进程对象其他的属性和方法

7.守护进程

8.僵尸进程与孤儿进程简单介绍

9.互斥锁

10.进程间通信(IPC机制)

11.生产者消费者模型

12.线程理论

13.开启线程的两种方式

14.线程对象的属性和方法

15.守护线程

16.线程互斥锁

17.全局解释器锁GIL

18.进程池与线程池

19.互斥锁与递归锁

20.IO模型



### 1.操作系统发展史

多道技术简介及图解

生活中的示例:洗衣烧水做饭

* 切换+保存状态(1.占用cpu过长时间切,效率低  2.遇到IO切,效率提升)

### 2.进程理论

进程与程序的区别

进程之间调度算法优化历程

* 时间片轮转法+多级反馈队列图示

进程的并行与并发及同步异步阻塞非阻塞

* 进程三状态图解(超市排队)

  尽量让自己的程序处于运行态或就绪态

  时间片正常用完，程序不会阻塞而是进入就绪

* 同步异步，阻塞非阻塞





### 3.创建进程的两种方式

```python
# 第一种自己定义函数
from multiprocessing import Process
import time

def task(name):
    print('%s is dsb'%name)
    time.sleep(1)
    print('%s is over'%name)
# windows操作系统下，创建进程一定要在main内创建，因为windows下创建进程类似于导模块的形式
# 会将开启它的进程的代码从头到位按照导模块的方式执行一遍，将产生的名字丢到新创建的进程内存中
if __name__ == '__main__':
    p = Process(target=task,args=('egon',))  # 实例化进程对象，注意传参
    # p = Process(target=task,kwargs={'name':'egon'})
    p.start()  # 告诉操作系统开启一个新的进程
    print('主')

# 第二种利用类的继承
# 类的继承
class MyProcess(Process):
    def run(self):
        print('hello big baby!')
        time.sleep(1)
        print('get out!')
if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('主')
```

### 4.join方法

```python
"""
1.介绍join方法、
2.多个进程多次join
3.for循环中join验证join特性
4.给函数加一个睡眠时间参数，主进程统计结束时间,join子进程先后顺序调换(最长的子进程时间多一点点)
5.将重复操作变成for循环的形式
"""
from multiprocessing import Process
import time

def task(name, n):
    print('%s is dsb' % name)
    time.sleep(n)
    print('%s is over' % name)

if __name__ == '__main__':
    start_time = time.time()
    p_list = []
    for i in range(1, 4):
        p = Process(target=task, args=('子进程%s' % i, i))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()
    print('主', time.time() - start_time)
"""join是让主进程等待子进程运行完毕，再结束。不影响子进程的运行"""
```

### 5.进程之间数据互相隔离

```python
from multiprocessing import Process
x = 100

def task():
    global x
    x = 222

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()  # 先不加这句没有说服力，加了这句才能有说服力
    print(x)
```

### 6.进程对象其他的属性和方法

```python
"""
1.current_process查看进程号
2.os.getpid() 查看进程号  os.getppid() 查看父进程进程号
3.进程的名字，p.name直接默认就有，也可以在实例化进程对象的时候通过关键字形式传入name=''

3.p.terminate()  杀死子进程 
4.p.is_alive()  判断进程是否存活	3，4结合看不出结果，因为操作系统需要反应时间。主进程睡0.1即可看出效果
"""

# 进程pid:每一个进程在操作系统内都有一个唯一的id号，称之为pid
from multiprocessing import Process,current_process
import time
import os
# os.getpid()查看当前进程	os.getppid()查看当前进程的父进程
# 主进程查看父进程id号，对应的是向操作系统发起开启进程的信号的人的id	可能是pycharm可能是终端

def task():
    print('%s is running'%current_process().pid)  # 查看当前进程id号
    time.sleep(30)  # 终端通过tasklist |findstr PID号验证
    print('%s is over'%current_process().pid)

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    print('主',current_process().pid)
# python代码都是被python.exe解释器执行的
```





### 7.守护进程

主进程死子进程立马就死(古代的陪葬)

```python
p.daemon = True  # 必须加在p.start()之前 加之后会报错
p.start()
```

### 8.僵尸进程与孤儿进程简单介绍

针对linux系统的，可讲可不讲。ps aux |grep "Z"查看僵尸进程

引子:进程与进程之间是相互独立的，但是为什么主进程还要等子进程结束才会结束呢？

所有的子进程在运行结束后都会变成僵尸进程，还保留着pid及占用cpu多长时间等信息。这些信息会被主进程主动回收(两种回收可能:1.主进程调用join的等待子进程结束回收。2.主进程正常结束调用wait回收)

孤儿进程：子进程还没结束，主进程先死了。意味着子进程的pid等信息不能被及时回收。要等到init回收机制来帮忙回收，会稍微熬时长一点

僵尸进程有害，父进程不死并且一直不停的在创建新的子进程

孤儿进程无害，因为有init管

### 9.互斥锁

将并发变成串行，牺牲效率保证数据的安全性，通常用于对数据的修改部分代码上

```python
# 1.先用join实现数据安全
# 2.不应该人为限制先后顺序，join不合适，只需要将买票变成串行即可
import json
from multiprocessing import Process,Lock
import random
import time

# 查看票
def search(i):
    with open('info','r',encoding='utf-8') as f:
        dic = json.load(f)
    print('用户%s查询余票:%s'%(i,dic.get('ticket_num')))

def buy(i):
    # 先查询数据库获取当前剩余票数
    with open('info','r',encoding='utf-8') as f:
        dic = json.load(f)
    # 模拟网络延迟
    time.sleep(random.randint(1,3))
    
    if dic.get('ticket_num') > 0:
        dic['ticket_num'] -= 1
        with open('info','w',encoding='utf-8') as f:
            json.dump(dic,f)
        print('用户%s买票成功'%i)
    else:
        print('用户%s买票失败'%i)

def run(i,mutex):
    search(i)
    mutex.acquire()
    buy(i)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()  # 要在主进程中生成互斥锁
    for i in range(10):
        p = Process(target=run,args=(i,mutex))
        p.start()
```









### 10.进程间通信(IPC机制)

```python
# 先来了解队列的概念   先进先出
from multiprocessing import Queue
q = Queue(5)  # 实例化一个q对象，参数可传可不传，用来限制队列的大小

# 步骤1；for循环放，演示超出范围阻塞情况
for i in range(6):
  q.put(i)  # 朝队列里放值

# 步骤2:手动一个个放
q.put(1~5)
q.full()  # 查看当前队列是否已满
q.get()  # 获取队列中的值，取多了也会阻塞住
q.empty()  # 判断队列是否取空了

# 两个地方需要注意，队列满了的时候，再放值会阻塞，直到前面的值被取走
# 队列空了的时候，再取值也会阻塞，直到有人再往这里面放值
q.get_nowait()  # 有值就拿，没值报错

"""
进程间使用队列传输数据
"""
# 步骤1:子进程生成数据，主进程获取打印
# 步骤2:子进程生成数据，另一个子进程获取数据
from multiprocessing import Queue,Process

def producer(q):
    q.put('hello big baby!')

def consumer(q):
    print(q.get())
    
if __name__ == '__main__':
    q = Queue()
    p = Process(target=producer,args=(q,))
    p.start()
    p1 = Process(target=consumer,args=(q,))
    p1.start()
```

### 11.生产者消费者模型

日常生活中买包子示例:(包子做的多了买的人少，包子做的少了买的人多)

程序中示例(一个程序负责生产数据，一个程序负责消费数据)

如何解决:弄一个存储数据的容器，满了就不再生产，不满就继续生产，无论生产的多还是消费的多，都可以很好的解决，生产的多就多开几个消费者进程，消费的多就多开几个生产者进程

总的来说就是如何解决生产与消费之间平衡的事情

```python
# 生产数据和消费数据都模拟一下延迟
# 先写两个生产者，生产数据,	再写一个消费者消费数据
# 再供需平衡 二对二
# 抛出问题 程序都最好生产者生产完消费者也消费完。还不结束如何处理?
# 主进程等待生产者的进程结束，然后往队列里丢一个None运行还是卡住
# 诠释队列中的数据多进程来获取是数据安全的，即对进程获取数据是加锁处理
# 主进程放两个None达到效果
# JoinableQueue使用

# 生产者消费者模型
from multiprocessing import Process, Queue
import time
import random

def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        data = '%s生产了%s%s' % (name, food, i)
        print(data)
        q.put(data)

def consumer(name, q):
    while True:
        # 这里不能用q.empty()判断队列是否为空，也不能用get_nowait()判断，因为都不精准
        food = q.get()
        if food is None: break
        time.sleep(random.randint(1, 3))
        print('%s吃了%s' % (name, food))

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=('egon', '包子', q))
    p2 = Process(target=producer, args=('kevin', '泔水', q))
    c1 = Process(target=consumer, args=('tank', q))
    c2 = Process(target=consumer, args=('owen', q))
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    # 我们想实现的就是在生产者生产完数据之后，通过队列告诉消费者已经没有数据可以再消费了
    p1.join()
    p2.join()
    q.put(None)
    # 先put一个，演示发现仍然阻塞，诠释队列对于进程获取里面的数据是加锁处理的
    q.put(None)
   
"""
上面的代码虽然解决了我们的问题，但是如果我再新增一个消费者，意味着我还要手动再往队列里添加None
"""
# 生产者消费者模型
from multiprocessing import Process, Queue,JoinableQueue
import time
import random

def producer(name, food, q):
    for i in range(3):
        time.sleep(random.randint(1, 3))
        data = '%s生产了%s%s' % (name, food, i)
        print(data)
        q.put(data)

def consumer(name, q):
    while True:
        # 这里不能用q.empty()判断队列是否为空，也不能用get_nowait()判断，因为都不精准
        food = q.get()
        if food is None: break
        time.sleep(random.randint(1, 3))
        print('%s吃了%s' % (name, food))
        q.task_done()  # 告诉队列，这个数据已经被我取出并处理完毕

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer, args=('egon', '包子', q))
    p2 = Process(target=producer, args=('kevin', '泔水', q))
    c1 = Process(target=consumer, args=('tank', q))
    c2 = Process(target=consumer, args=('owen', q))
    p1.start()
    p2.start()

    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    # 我们想实现的就是在生产者生产完数据之后，通过队列告诉消费者已经没有数据可以再消费了
    p1.join()
    p2.join()
    # q.put(None)
    # # 先put一个，演示发现仍然阻塞，诠释队列对于进程获取里面的数据是加锁处理的
    # q.put(None)
    q.join()  # 等待队列中的数据全部被取出
    print('主')  # 能走到这一步说明生产者已经生产完所有的数据，消费者也已经消费了所有的数据
```







### 12.线程理论

```python
"""
1.什么是线程？
	进程:资源单位(起一个进程仅仅只是在内存中开辟一块空间)
	线程:执行单位(真正被cpu执行的其实是线程，线程其实指的就是代码的执行过程,执行代码中需要的数据找进程这个资源单位要！)
也就意味着进程中真正在执行功能的其实是它里面的线程，即每个进程内部都必须起码有一个线程

2.为什么要有线程？
# 1.同一个进程下的多个线程共享该进程内的资源
# 2.创建线程的开销要远远小于进程
	再来举例阐述
		开发一个文本编辑器工具,功能获取用户输入并显示到屏幕上并适时存入硬盘
"""
```

### 13.开启线程的两种方式

同开启进程的方式一样

### 14.线程对象的属性和方法

```python
# 1.验证线程之间数据共享
from threading import Thread
import time
n=100
def task():
    global n
    n=0
if __name__ == '__main__':
    t=Thread(target=task)
    t.start()
    t.join()
    print('主',n)
    
# 2.线程之间os.getpid() >>> 相等
from threading import Thread
import time,os
def task():
    print('%s is running' %os.getpid())
if __name__ == '__main__':
    t=Thread(target=task)
    t.start()
    print('主',os.getpid())

# 3.active_count当前活跃的线程个数,当前线程
from threading import Thread,active_count,current_thread
import time,os
def task():
    print('%s is running' %current_thread().name)
    time.sleep(2)
if __name__ == '__main__':
    t=Thread(target=task,)
    t.start()
    # t.join()
    # print('主',active_count())
    print('主',current_thread().name)
```

### 15.守护线程

```python
# 进程自带的那个线程运行结束，守护线程立即结束
"""
主线程会等待所有非守护线程的结束，原因在于主线程结束意味着当前进程结束，空间资源均被回收
很明显子线程可能还在运行，明显不合理！
"""
from threading import Thread
import time
def task(name):
    print('%s is running' %name)
    time.sleep(2)
    print('%s is done' %name)
if __name__ == '__main__':
    t=Thread(target=task,args=('线程1',))
    t.daemon=True
    t.start()
    print('主')
# 稍微有点迷糊人的例子
from threading import Thread
from multiprocessing import Process
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")
def bar():
    print(456)
    time.sleep(3)
    print("end456")
if __name__ == '__main__':
  	t1=Thread(target=foo)
    t2=Thread(target=bar)
    t1.daemon=True
    t1.start()
    t2.start()
    print("main-------")
"""
123
456
main-------
end123
end456
"""
```

### 16.线程互斥锁

```python
from threading import Thread,Lock
import time

mutex=Lock()  # 创建线程不需要从头到位再执行代码拷贝数据
n=100
def task():
    global n
    mutex.acquire()
    temp=n
    time.sleep(0.1)
    n=temp-1
    mutex.release()

if __name__ == '__main__':
    t_l=[]
    for i in range(100):
        t=Thread(target=task)
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()
    print(n)
```





### 17.全局解释器锁GIL

```cmd
'''
定义：
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple 
native threads from executing Python bytecodes at once. This lock is necessary mainly 
because CPython’s memory management is not thread-safe. (However, since the GIL 
exists, other features have grown to depend on the guarantees that it enforces.)
'''
结论：在Cpython解释器中，同一个进程下开启的多线程，同一时刻只能有一个线程执行，无法利用多核优势

# 画图诠释
“”“
单核情况下:四个任务
多核情况下:四个任务

计算密集型:一个任务算十秒,四个进程和四个线程，肯定是进程快
IO密集型:任务都是纯io情况下，线程开销比进程小，肯定是线程好
”“”
```

* GIL其实就是一把互斥锁(牺牲了效率但是保证了数据的安全)。
* 线程是执行单位，但是不能直接运行，需要先拿到python解释器解释之后才能被cpu执行
* 同一时刻同一个进程内多个线程无法实现并行，但是可以实现并发
* 为什么要有GIL是因为它内部的垃圾回收机制不是线程安全的
* 垃圾回收机制也是一个任务，跟你的代码不是串行运行，如果是串行会明显有卡顿
* 这个垃圾回收到底是开进程还是开线程？肯定是线程，线程肯定也是一段代码，所以想运行也必须要拿到python解释器
* 假设能够并行，会出现什么情况？一个线程刚好要造一个a=1的绑定关系之前，这个垃圾线程来扫描，矛盾点就来了，谁成功都不对！
* 也就意味着在Cpython解释器上有一把GIL全局解释器锁
* 同一个进程下的多个线程不能实现并行但是能够实现并发，多个进程下的线程能够实现并行

代码验证

```python
​```python
# 计算密集型
from multiprocessing import Process
from threading import Thread
import os,time
def work():
    res=0
    for i in range(100000000):
        res*=i


if __name__ == '__main__':
    l=[]
    print(os.cpu_count())  # 本机为12核
    start=time.time()
    for i in range(12):
        # p=Process(target=work) #耗时8s多
        p=Thread(target=work) #耗时44s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))

# IO密集型
from multiprocessing import Process
from threading import Thread
import threading
import os,time
def work():
    time.sleep(2)


if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为12核
    start=time.time()
    for i in range(400):
        p=Process(target=work) #耗时12s多,大部分时间耗费在创建进程上
        # p=Thread(target=work) #耗时2s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))
```





### 18.进程池与线程池

无论是开进程还是开线程，无限制的开下去都会对计算机硬件造成极大的压力，为了在保证硬件安全的情况下最大可能的提升程序运行效率，应该采用池

线程池创建,线程数验证,往池里面提交任务的方式是异步提交,回调函数,

```python
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time
import os
# 示例化池对象
# 不知道参数的情况，默认是当前计算机cpu个数乘以5，也可以指定线程个数
# pool = ThreadPoolExecutor(20)  # 创建了一个池子，池子里面有20个线程
pool = ProcessPoolExecutor(5)  # 创建了一个池子
def task(n):
    print(n,os.getpid())
    time.sleep(2)
    return n**2
def call_back(n):
    print('我拿到了结果:%s'%n.result())
"""
提交任务的方式
    同步:提交任务之后，原地等待任务的返回结果，再继续执行下一步代码
    异步:提交任务之后，不等待任务的返回结果(通过回调函数拿到返回结果并处理)，直接执行下一步操作
"""
# 回调函数:异步提交之后一旦任务有返回结果，自动交给另外一个去执行
if __name__ == '__main__':
    # pool.submit(task,1)
    t_list = []
    for i in range(20):
        future = pool.submit(task,i).add_done_callback(call_back)  # 异步提交任务
        t_list.append(future)

    # pool.shutdown()  # 关闭池子并且等待池子中所有的任务运行完毕
    # for p in t_list:
    #     print('>>>:',p.result())
    print('主')
```

### 19.互斥锁与递归锁

```python
from threading import Thread,Lock,RLock
import time

# mutexA=Lock()
# mutexB=Lock()
mutexB=mutexA=RLock()


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
```

### 20.IO模型

