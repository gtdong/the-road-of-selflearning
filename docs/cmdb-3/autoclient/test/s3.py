import time

### 线程池

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


def run(i):
    time.sleep(2)
    print(i)

p = ThreadPoolExecutor(10)
for i in range(10):
    # run(i)
    p.submit(run,i)