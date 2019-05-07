def foo():
    print('Generator-Start')

    aaa = yield 1  # Fighting!
    print(aaa)

    bbb = yield 2
    print(bbb)

    yield 3

f1 = foo()  # 创建Generator函数

a1 = f1.send(None)  # 执行Generator函数内部代码至第一个yield
a2 = f1.send("aaa")  # yield 1 表达式的值 变为 "aaa"
a3 = f1.send('bbb')  # yield 2 表达式的值 变为 "bbb"

print(a1, a2, a3)  # 1, 2, 3
