from multiprocessing import Process


money = 10000000000000


def task():
    global money
    money = 0
    print('我真的运行了 没骗你')


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print(money)