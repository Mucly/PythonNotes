# 适合 处理I/O密集型 场合
# 注：多线程共享一块内存区域
import threading


def foo(arg1):
    print(f"{arg1}")

if __name__ == "__main__":
    th1 = threading.Thread(target=foo, args=("th1",))  # 开一个线程
    th1.start()  # 启动线程
    th1.join()  # 等待结束
