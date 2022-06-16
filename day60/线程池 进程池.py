from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def func(name):
    for i in range(1000):
        print(i, name)


if __name__ == '__main__':
    start = time.time()
    # with ThreadPoolExecutor(20) as t:  # 线程池 2.6s
    with ProcessPoolExecutor(20) as t:  # 进程池 0.8s
        for i in range(100):
            t.submit(func, name=f'线程{i}')
    end = time.time()
    print('done', end - start)
