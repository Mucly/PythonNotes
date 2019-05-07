# 异步IO协程范例
import threading
import asyncio

async def hello(name):  # Python 3.5
    print('Hello %s (%s)' % (name, threading.currentThread()))
    await asyncio.sleep(1)  # 模拟IO操作 # 此处切换至下个task, 本task的IO完成后，继续执行下面的代码
    print('Bye %s (%s)' % (name, threading.currentThread()))

#　PART 1 获取一个事件loop
loop = asyncio.get_event_loop()

# PART 2 封装三个coroutine函数 eg. [ func(arg), func(arg), func(arg) ]
tasks = [hello(name) for name in ["阿花", "阿猫", "阿三"]]

# PART 3 单线程并发
loop.run_until_complete(asyncio.wait(tasks))

# PART 4 关闭
loop.close()

''' >>>
        Hello 阿猫 (<_MainThread(MainThread, started 5004)>)
        Hello 阿花 (<_MainThread(MainThread, started 5004)>)
        Hello 阿三 (<_MainThread(MainThread, started 5004)>)
        Bye 阿猫 (<_MainThread(MainThread, started 5004)>)
        Bye 阿花 (<_MainThread(MainThread, started 5004)>)
        Bye 阿三 (<_MainThread(MainThread, started 5004)>)
'''
