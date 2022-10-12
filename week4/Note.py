# -----------------------作用域----------------------------------------------------
# 变量/函数的查找顺序：Local(局部作用域) -> Enclosing(闭包函数外的函数中) -> Global(全局作用域) -> Built-in(内建作用域)
# （优先在当前作用域中寻找，如果没有在上一级中寻找）
# 外部不能访问到内部，内部可以访问外部

# 全局作用域：
#   全局作用域在程序执行时创建，在程序执行结束时销毁
#   所有函数意外的区域都是全局作用域
#   在全局作用域中定义的变量，都属于全局变量，全局变量可以在程序的任意位置被访问（函数名也是全局变量）

# 函数作用域
# 函数作用域在函数调用时创建，在调用结束时销毁
# 函数每调用一次就会产生一个新的函数作用域
# 在函数作用域中定义的变量，都是局部变量，它只能在函数内部被访问

# 在函数中为变量赋值时，默认都是为局部变量赋值
# 如果希望在函数内部修改全局变量，则需要使用global关键字，来声明变量

from glob import glob


name1='david'

def name():
    # name1='joyce'
    global name1 #修改全局变量
    name1='joyce'

    print(name1)
    return name1

name()
print(name1)


# 命名空间（namespace）（变量存储的位置）
# 全局命名空间。用来保存全局变量；函数命名空间用来保存函数中的变量
# locals()用来获取当前作用域的命名空间（字典）
scope=locals()
print(scope)

def fn():
    a=10
    scope1=locals()
    scope2=globals() # 获取全局命名空间
    print(scope2)
    print(scope1)

fn()

# globals() ：以dict的方式存储所有全局变量
def foo():
    print("I am a func")


def bar():
    foo = "I am a string"
    foo_dup = globals().get("foo")
    foo_dup()


bar()

# locals()：以dict的方式存储所有局部变量
other = "test"


def foobar():
    name = "MING"
    gender = "male"
    dic=locals().items()
    print(dic)
    for key, value in locals().items():
        print(key, "=", value)

foobar()



# -----------------------高阶函数----------------------------------------------------
# 在python中，函数是一等对象：
#   1.对象是在运行时创建的
#   2.能赋值给变量或作为数据结构中的元素
#   3.能作为参数传递
#   4.能作为返回值范围

# 高阶函数：
#   1.接受一个或多个函数作为参数
#   2.将函数作为返回值返回

def fn2(n):
    if n%2==0:
        return True
    return False

def fn3(n):
    if n>5:
        return True
    return False

def fn1(func,lst):

    lst1=[]
    for n in lst:
        # if n%2==0:
        if func(n):
            lst1.append(n)
            
    
    return lst1

l=[1,2,3,4,5,6,7,8,9,10]
print(fn1(fn2,l))
# 只写函数名表示将函数作为参数传递，函数名加括号表示调用函数


# filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
# 参数：1.函数（过滤条件）；2.可迭代的结构
# 返回值：过滤后的新的可迭代的结构
print(list(filter(fn2,l)))

# 匿名函数（lambda函数表达式）：lambda 参数列表: 返回值
print((lambda a,b: a+b)(1,2))

print(list(filter(lambda n:n%2==0,l)))


# map()可以对可迭代对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回
r=map(lambda n: n+1,l)
print(list(r))


# -----------------将函数作为参数的高阶函数举例---------------------
# sort()对列表中的元素进行排序
# sort()可以接收一个关键字参数，key，需要一个函数作为参数
# 每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
l1=['aa','hhhhd','ajshdue','dddd','z']
l1.sort(key=len)
print(l1)

l2=[1,2,'3','6',5]
l2.sort(key=int)
print(l2)

# sorted()可以对任意的序列进行排序，不影响原来的对象，返回一个新的对象
l3='192837402839'
print(sorted(l3,key=int))


# -----------------将函数作为返回值返回 （闭包）---------------------
# fn5()函数在fn4()内部定义，不是全局函数，所以这个函数总是能访问到fn4()函数内的变量
# 通过闭包可以创建一些只有当前函数能访问的变量（可以将一些私有的数据藏到闭包中）
def fn4():
    num=10

    def fn5():
        print(num)

    return fn5

r=fn4()
r()

# 形成闭包的要件：函数嵌套；将内部函数作为返回值返回；内部函数必须要使用外部函数的变量
def make_average():
    nums=[]

    def averager(n):
        nums.append(n)
        return sum(nums)/len(nums)
    
    return averager

ave=make_average()
print(ave(1))
print(ave(2))
print(ave(4))

# 闭包案例一： 打印分割线案例
#  定义的line函数调用参数太多，不方便在多处调用
def line(symbol, title, numbers):
    half_part_symbols = (numbers // 2) * symbol
    print(half_part_symbols + title + half_part_symbols)

line('-', '华丽丽的分割线', 20)
line('*', '我是星星分割线', 40)

# 利用闭包，方便了同一类型line在多处调用的场景
def line_config(symbol, title, numbers):
    def wrapper():
        half_part_symbols = (numbers // 2) * symbol
        print(half_part_symbols + title + half_part_symbols)

    return wrapper

dashed_line = line_config('-', '华丽丽的分割线', 20)
star_line = line_config('*', '天上的星星不说话', 40)
dashed_line()
star_line()

# 闭包案例二： 连续走步，统计走完之后总共走了多少步
def count_steps(original_steps=0):
    def wrapper(new_steps):
        nonlocal original_steps  # 添加nonlocal是为了改变外函数中的变量original_steps的值
        # print(original_steps)
        total_steps = original_steps + new_steps
        original_steps = total_steps
        return original_steps

    return wrapper

go = count_steps(8)
print(go(2))
print(go(3))
print(go(5))
print(go(5))

# 注意变量的变化
def func_2():
    i = 'I am a closure function'

    def wrapper():
        print(i, 'in func_2')

    i = 888
    return wrapper

func_2()()

def func_3():
    list_funcs = []
    for i in range(1, 5):
        def wrapper():
            print(i)

        list_funcs.append(wrapper)
        print(list_funcs)

    return list_funcs

func_3()[0]()

# 修改后
def func_4():
    list_funcs = []
    for i in range(1, 5):
        def wrapper(i):
            # print(i)
            def inner():
                print(i)

            return inner

        list_funcs.append(wrapper(i)) #wrapper(i)被立即执行
        # print(list_funcs)
    return list_funcs

func_4()[0]()
func_4()[1]()
func_4()[2]()
func_4()[3]()

# 闭包函数的__closure__里面，定义了一个元组用于存放所有的cell对象，每个cell对象保存了这个闭包中所有的外部变量。
# 如果嵌套函数wrapper引用的是j，则不会产生闭包
j = 'Hi'
def func_demo():
    i = 'Hello'

    def wrapper():
        print(i)

    return wrapper

func_wrapper = func_demo()
func_wrapper()
print("closure function's variables: ",
      func_wrapper.__closure__[0].cell_contents)
for x in func_wrapper.__closure__:
    print(x.cell_contents)

# 检测不返回嵌套函数名wrapper，是否构成闭包
def func_demo_2():
    i = 'Hello'
    print(func_demo.__code__.co_cellvars)  # 自由变量的名字

    def demo():
        def wrapper():
            print(i)
            # 一个函数和它的环境变量（又叫自由变量）组合在一起，就构成了一个闭包(closure)。环境变量取值被保存在函数对象的__closure__属性中,且cell_contents是cell对象的唯一属性
            print("自由变量的值",wrapper.__closure__[0].cell_contents)  # 自由变量的值
            print("自由变量的名字",wrapper.__code__.co_freevars)  # 自由变量的名字
        wrapper()
    # 不返回函数名，也能构成闭包
    # return wrapper
    demo()

func_demo_2()
print('999', func_demo_2.__closure__) # func_demo_2()不是闭包函数
print(dir(func_demo_2))

def demo():
    pass

print(demo.__closure__)  # 普通函数也有__closure__，但不是闭包
print(dir(demo))
demo()
print(demo)



# --------------------------------------装饰器--------------------------------------------
# 在不改变原函数的情况下，对函数进行扩展 （装饰器）
def begin_end(old):

    def new_function(*args,**kw):
        print('开始执行---')
        result=old(*args,**kw)
        print('结束执行---')
        return result 
    
    return new_function

def fn5(a,b):
    print(a+b)

def fn6():
    print('fn6')

r1=begin_end(fn5)
r1(2,6)

r2=begin_end(fn6)
r2()

def begin_end1(old):

    def new_function(*args,**kw):
        print('1开始执行---')
        result=old(*args,**kw)
        print('1结束执行---')
        return result 
    
    return new_function

# 在定义函数时，可以通过@装饰器，来使用指定的装饰器，来装饰当前的函数
# 可以同时为一个函数指定多个装饰器，函数将会从内向外的顺序被装饰
@begin_end
@begin_end1
def say_hello():
    print('hello!')

say_hello()