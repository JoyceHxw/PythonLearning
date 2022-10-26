# 1---------------------------------------------------
from textwrap import wrap


def get_time(func):
    def wrapper():
        func()
        print("used time: xxx")
    return wrapper

@get_time
def foo():
    print("foo")

foo()

def foo1():
    print("foo")
    print("used time: xxx")

foo1()



# 2---------------------------------------------------
def f_a(func):
    print("f_a")

    def w_a():
        print(1)
        func()
    return w_a

def f_b(func):
    print("f_b")

    def w_b():
        print(2)
        func()
    return w_b

@f_a
@f_b
def f_c():
    print("f_c")
    print(3)

f_c()

# f_a(f_b(f_c))()


def make_bold(fn):
    def wrapped():
        return "<b>"+fn()+"</b>"
    
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>"+fn()+"</i>"
    return wrapped

@make_bold
@make_italic
def hello():
    return "hello world"

print(hello())


# 3---------------------------------------------------
def decorator(func):
    def wrapper(**kwargs):
        print("call function")
        return func(**kwargs)
    return wrapper

@decorator
def foo(**kwargs):
    print("this is foo")
    print(kwargs)

foo(name="joyce",age=18)


# 4---------------------------------------------------
def func_out(info):
    def decorator(func):
        def wrapper():
            print(info)
            print("call function")
            return func()
        return wrapper
    return decorator

@func_out(info="hello")
def foo():
    print("this is foo")

foo()
# func_out(info="hello")(foo)()