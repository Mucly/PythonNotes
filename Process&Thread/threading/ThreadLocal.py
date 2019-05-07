# 设置当前线程的全局变量
# 场合：当前线程下，各函数的实参重复较多的情况下
import threading

# 创建全局ThreadLocal对象:
local_student = threading.local()  # <class：dict>


def process_student():
    # 获取当前线程关联的student:
    name = local_student.name
    print('Hello, %s (in %s)' % (name, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student_name
    local_student.name = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')

t1.start()
t2.start()

t1.join()
t2.join()
