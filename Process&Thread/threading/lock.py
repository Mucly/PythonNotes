# 进程锁实例： 银行存取款
# GIL的存在，导致多线程只能在单核上跑
import threading

balance = 100  # 假设账户余额初始有100块
lock = threading.Lock()  # 进程锁


def change_money(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000000):
        lock.acquire()  # 获取锁
        try:
            change_money(n)
        finally:
            lock.release()  # 释放锁， try的方式，确保释放
