# 多线程，适合 计算（CPU）密集型 场合, 切换耗时
from multiprocessing import Process, Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def print_msg(i):
    print(f"Process{i} End in {time.time()}")

if __name__ == '__main__':
    # --- Note 1 子进程的基本使用
    p1 = Process(target=long_time_task, args=(0,))  # args must be iterated， here is set_object
    p1.start()  # 启动
    p1.join()  # 连接: 等待p1子进程结束后再往下执行，通常用于子进程间的同步

    # --- Note2 子进程池（用于开启大量子进程）
    CORE_CNT = 4
    procs_pool = Pool(CORE_CNT)  # 形参缺省为本机cpu核心数
    for i in range(CORE_CNT):
        procs_pool.apply_async(print_msg, (i,))
    procs_pool.close()
    procs_pool.join()  # pool对象调用join前必须close，执行完close后不会有新的进程加入到pool, join函数等待所有子进程结束
