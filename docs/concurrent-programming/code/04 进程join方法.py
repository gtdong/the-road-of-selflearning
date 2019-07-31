from multiprocessing import Process
import time

def task(name,n):
    print('%s is running' % name)
    time.sleep(n)
    print('%s is end'%name)


if __name__ == '__main__':
    start_time = time.time()
    p_list = []
    for i in range(1,4):
        p = Process(target=task,args=('子进程%s'%i,i**i))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()
    # p.join()  # 会将程序变成串行
    # p1 = Process(target=task,args=('jason',1))
    # p2 = Process(target=task,args=('egon',2))
    # p3 = Process(target=task,args=('echo',3))
    # p1.start()  # 仅仅只是告诉操作系统你需要创建一个进程
    # p2.start()
    # p3.start()
    # time.sleep(4)
    # p.join()  # 主进程等待指定的子进程运行结束之后才执行  不影响其他子进程的运行
    # p3.join()
    # p1.join()
    # p2.join()
    print('主')
    print('耗时:%s'%(time.time() - start_time))
    # p = Process(target=task,kwargs={'name':'jason'})