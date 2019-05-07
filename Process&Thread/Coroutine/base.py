# 协程范例：生产者-消费者模式
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        # print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # 等同c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 第一次循环时，将yield表达式（即yield r语句）变为1，故consumer函数内变量n == 1，然后代码继续向下执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  # 中断generator

c = consumer()  # generator函数，在实际运行（c.send(n) / c.next()）时，才会真正的执行其内部代码
produce(c)
