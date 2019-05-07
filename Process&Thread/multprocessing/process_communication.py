# 进程之间的通讯范例
from multiprocessing import Process, Queue
import os
import time
import random


def write(q):
    ''' 写数据进程 '''
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    ''' 读数据进程，死循环，直至成功获取结果 '''
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()  # 启动子进程pw，写入
    pr.start()  # 启动子进程pr，读取

    pw.join()  # 等待pw结束
    pr.terminate()  # 强行终止用于接受消息的pr进程（死循环）
