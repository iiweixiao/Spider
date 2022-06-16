from threading import Thread
from multiprocessing import Process


# 多线程
# 方法一：
def func(name):
    for i in range(1000):
        print('func', i, name)


# Process和Thread关键词互掉即可切换多进程和多线程
if __name__ == '__main__':
    t1 = Thread(target=func, args=('Jay',))
    t1.start()
    t2 = Thread(target=func, args=('Tony',))
    t2.start()
    for i in range(1000):
        print('main', i)

# 方法二：
# class MyThread(Thread):
#     def run(self):
#         for i in range(1000):
#             print('func', i)
#
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()
#     for i in range(1000):
#         print('main', i)
