from multiprocessing import Process
import time

def task(name):
    print('%s 还活着'%name)
    time.sleep(3)
    print('%s 正在死亡'%name)

if __name__ == '__main__':
    p = Process(target=task,args=('egon总管',))
    # p.daemon = True  # 将进程p设置为当前主进程的守护进程
    p.start()
    # p.daemon = True  一定要写在p.start之前
    time.sleep(1)
    print('皇帝jason驾崩了')