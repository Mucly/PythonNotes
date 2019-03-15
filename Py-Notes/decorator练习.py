import functools


def log(temp):
    if callable(temp):  # 如果形参是函数，eg.@log \def func():\pass
        func = temp
        @functools.wraps(func)
        def wrapper(*argvs, **kw):
            print('%s %s():' % ('go', func.__name__))
            return func()
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)  # 防止__name__变为wrapper
            def wrapper(*args, **kw):
                print('%s %s():' % (temp, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

# @log
@log('start')
def now():
    print('2015-3-25')


now()  # 等同于 log('execute')(now)
