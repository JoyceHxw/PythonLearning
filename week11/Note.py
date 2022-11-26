# 描述器
# __getattribute__(self,name)：实例属性访问拦截器，在对类实例属性和方法访问时，此方法均会被无条件调用
#       如实例a有属性x，a.x将从a.__dict__['x']查找，如果x为数据描述器实例，则执行描述器中的__get__方法并返回值
#       如果x为非数据描述器，且a有x属性，则返回x的值，否则执行非数据描述器中__get__方法并返回值
#       以上皆否，则基于type(a)的mro顺序向上查找，直到找到或报错
#       在自定义的类中重写__getattribute__()方法，可拦截对象属性的所有访问，从而达到只能访问部分权限，实现数据封装的效果
# __getattr__(self,name)：当调用实例属性引发AttributeError失败时被调用，调用__getattr__前必会调用__getattribute__，定义了__getattr__方法之后，外部函数getattr()第三个参数不再起作用
# __get__：__getattribute__方法调用描述器实例时，会在描述器中触发的方法
# 函数getattr(object, name, default): 如果字符串name是对象object的属性之一的名称，则返回name对应的值，否则返回默认值（注意name里要加引号）
# 函数hasattr(object, name)：如果字符串name是对象object的属性之一的名称，则返回True，否则返回False
# 函数setattr(object, name, value)：本函数与getattr()相对应，其参数为一个对象、一个字符串和一个任意值。字符串可以为某些现有属性的名称或新属性，只要对象允许，函数会将值赋给属性

class A:
    v=5

    def __init__(self,x) -> None:
        self.x=x
    
    def func(self):
        return "Func function"

a=A(10)
print(getattr(a,"x"))
print(getattr(a,"y",20))
print(getattr(a,"func")())
print(getattr(A,"v"))
# print(getattr(a,"y"))   # 没有y属性

print("---------------------------------")
class A1:
    x=66
    print("class attribute...")

    def __init__(self,x) -> None:
        self.x=x
        print("initial...")
    
    def func(self):
        return "func function"
    
    def __getattr__(self, item):
        print("in __getattr")
        return 100
    
    def __getattribute__(self, item):
        print("in __getattribute__")
        return super().__getattribute__(item)

a1=A1(10)
a1.x=55
print(a1.x)
print(a1.y)
print(a1.func())
print(A1.x)    # 通过类调用，查找的逻辑在type.__getattribute__()中



print("---------------------------------")
class M:
    def __init__(self) -> None:
        print("init class M")
        self.x=1
    
    def __get__(self,instance,owner):
        print("get m here")
        return self.x
    
    def __set__(self,instance,value):
        print("set m here")
        self.x=value+1
    
class N:
    def __init__(self) -> None:
        print("init class N")
        self.x=1
    
    def __get__(self,instance,owner):
        print("get n here")
        return self.x
    
class A2:
    m=M()
    n=N()

    def __init__(self,m,n) -> None:
        print("init class A")
        self.m=m
        self.n=n

a2=A2(2,5)
print(a2.__dict__)
print(A2.__dict__)
print(a2.n)
print(A2.n)
print(a2.m)
a2.m=6
print(a2.m)
print("---分隔符---")
print(A2.__dict__["n"].__get__(None,A2))
print(A2.__dict__["n"].__get__(a2,A2))


print("---------------------------------")
class X:
    def __init__(self,x) -> None:
        print("class X init...")
        self.x=x

    def __get__(self,instance,owner):
        print("in __get__")
        return self.x

    def __set__(self,instance,value):
        print("in __set__") 
        instance.__dict__["x"]=value    # 指定字典中的键，会触发__getattribute__
        print("*********************")
        print(instance.__dict__["x"]) 

class A3:
    x=X(0)
    print("class attribute...")

    def __init__(self,x) -> None:
        self.x=x
        print("class A's instance init...")

    def func(self):
        return "func function"
    
    def __getattr__(self,item):
        print("in __getattr__")
        return 100
    
    def __getattribute__(self, item):
        print("in __getattribute__")
        print("item:",item)
        return super().__getattribute__(item)

a3=A3(10)
a3.x=55
print(a3.x)
print(a3.y)
print(a3.func())
print(A3.x)
print(a3.__dict__)
print(a3.x)
print("a3.y=",a3.y)
print(a3.__dict__)
q=getattr(a3,"p",88)    # 被忽略掉，用__getattr__
print("q:",q)
print(a3.__dict__)



print("---------------------------------")
class A4:
    def __init__(self,x) -> None:
        self.x=X
    
    def __getattr__(self,name):
        print("in __getattr__")
        return 100
    
    def __getattribute__(self,name):
        print("in __getattribute__")
        print(name)
        return super().__getattribute__(name)
a4=A4(10)
print("*******")
a4.__dict__={"z:": 99}   # 不会触发__getattr__
print("^^^^^^^")
print(vars(a4))



print("---------------------------------")
# __getattribute__陷阱
class A5(object):
    Cnum=10

    def __init__(self,inum) -> None:
        self.inum=inum
    
    def __getattribute__(self, name):
        print(f"正在查找{name}")
        try:
            # return self.name  # 错误，会陷入循环
            return object.__getattribute__(self,name)
        except AttributeError:
            print(f"没有找到:{name}")



print("---------------------------------")
# 属性描述器
class C:
    def __init__(self) -> None:
        self._x=None
    
    @property
    def x(self):
        print("I'm the x property")
        return self.x
    
    @x.setter
    def x(self, value):
        print("in set...")
        self._x=value
    
    @x.deleter
    def x(self):
        del self._x
c=C()
print(c._x)
c._x=10
print(c._x)


print("---------------------------------")
# __new__(cls, *args, **kwargs)：构造方法，创建并返回一个实例对象
# 必须要有返回值，返回实例化出来的实例，若没有正确返回当前类cls的实例，__init__方法不会被调用，即便是父类的实例也不行
class A6:
    pass

class B(A6):
    def __init__(self) -> None:
        print("__init__被调用")
    
    def __new__(cls, *args, **kwargs):
        print("__new__被调用")
        print("cls: ", cls, id(cls))
        return object.__new__(A6)  # 错误，应该写B

b=B()
print("b: ",b)
print("A: ",A,id(A))
print("B: ",B,id(B))



print("---------------------------------")
# 单例模式
def singleton(cls, *args, **kw):
    instance={}
    def _singleton(*args, **kw):
        if cls not in instance:
            instance[cls]=object.__new__(cls, *args, **kw)
            print(instance)
        else:
            print(instance)
            print("已存在该类实例")
    return _singleton
 
@singleton
class test_singleton(object):
    def __init__(self):
        self.num_sum=0
    def add(self):
        self.num_sum=100

t=test_singleton()
t2=test_singleton()



print("---------------------------------")
class Singleton:
    instance={}
    def __init__(self) -> None:
        print(111)
    
    def __call__(self,cls):
        def wrapper(*args,**kw):
            print(222)
            if cls not in self.instance:
                print(333)
                print(self.instance)
                self.instance[cls]=object.__new__(cls, *args, **kw)
            else:
                print(self.instance)
                print("已存在该类实例")
            return self.instance
        return wrapper

@Singleton()
class test1_singleton(object):
    def __init__(self):
        self.num_sum=0
    def add(self):
        self.num_sum=100

s=test1_singleton()
# s.add()
s2=test1_singleton()



print("---------------------------------")
# define our own classmethod decorator
class myClassMethod():
    # init a Decorator obj, see the Decorator protocol here: https://docs.python.org/3/glossary.html#term-descriptor
    def __init__(self,func):
        self._func = func
    
    # Decorator obj as an attibute, this method handlers the getattr call.
    def __get__(self, obj, obj_type):
        # warp the original function
        def wrapper(*args,**kargs):
            print(obj)
            return self._func(obj_type, *args, **kargs)
        return wrapper

class myStaticMethod():
    def __init__(self, func):
        self._func = func
    def __get__(self, obj, obj_type = None):
        return self._func


# try it
class Test:
    @myClassMethod
    def hello(cls):
        print("world.")

    @myStaticMethod
    def sum(a, b):
        return a+b

t = Test() 

# works as classmethod and staticmethod does.

Test.hello()    # world
t.hello()       # world
print(type(t.hello()))

print(Test.sum(1, 2)) # 3
print(t.sum(1, 2))    # 3