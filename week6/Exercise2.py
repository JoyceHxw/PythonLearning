# 1. 请实现一个装饰器，通过一次调用使函数重复执行5次。
#   - 之后改写为给装饰器传递参数的形式来指定重复次数，

def circulation(n):
    def decorator(fn):
        def wrapper():
            for _ in range(n):
                fn()
        return wrapper
    return decorator

@circulation(5)
def foo():
    print("this is foo")

foo()
