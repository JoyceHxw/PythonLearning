from abc import ABC, ABCMeta, abstractmethod

# 继承的MRO顺序
class O:
    pass
class D(O):
    pass
class E(O):
    pass
class F(O):
    pass
class B(D,E):
    pass
class C(E,F):
    pass
class A(B,C):
    pass

print(A.__mro__)   #(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class '__main__.F'>, <class '__main__.O'>, <class 'object'>)


# type()函数：type(obj)获取obj的类型，不考虑继承关系
# type()函数既可以返回一个函数的类型，也可以创建出新的类型
# type是创建类的类（元类）
print("-------------------------------")
a=A()
print(type(a))  # <class '__main__.A'>
print(type(A))  # <class 'type'>
print(type(B))  # <class 'type'>
print(type(O))  # <class 'type'>
print(type(object))  # <class 'type'>


# 通过继承type类，可修改创建类的方式，通过metaclass=声明类的创建方式，
# 使用元类创建类时，其__new__()方法会自动执行，用来修改新建类
class ModelMeta(type):
    def __init_subclass__(cls, *args, **kwargs) -> None:
        super().__init_subclass__(*args, **kwargs)
        print("init a", cls)
        print("init a", cls.__class__.__name__)

class Model(metaclass=ModelMeta):
    pass

print(Model.__mro__)  # (<class '__main__.Model'>, <class 'object'>)  类Model相当于ModelMeta的实例
print(ModelMeta.__mro__)  # (<class '__main__.ModelMeta'>, <class 'type'>, <class 'object'>)
print(Model())
print(type(Model),type(ModelMeta))



# 抽象基类和抽象方法
# 包含抽象方法的类只能被继承，不能被实例化，且子类必须实现抽象方法
print("-------------------------------")
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass

class AliPay(Payment):
    def pay(self, money):
        print(f"支付宝支付：{money}元")

ali=AliPay()
ali.pay(100)


# 描述器
print("-------------------------------")
class Ten:
    def __get__(self, obj, objtype=None):
        return 10

class T:
    x=5
    y=Ten()

t=T()
print(t.x)
print(t.y)

t.z=Ten()
print(t.z)


# 硬耦合
print("-------------------------------")
class LoggedAgeAccess:
    def __get__(self,obj, objtype=None):
        value=obj._age
        print(f"Accessing 'age' giving {value}")
        return value
    
    def __set__(self,obj,value):
        print(f"Updating 'age' to {value}")
        obj._age=value
        print("value=",value)
        print("obj._age=",obj._age)
        print("in set...")

class Person:
    age=LoggedAgeAccess()

    def __init__(self,name,age):
        self.name=name
        print(111)
        self.age=age  # 修改赋值会触发setter
        print("age=",age)
        print(222)
    
    def birthday(self):
        print(333)
        self.age += 1
        print(444)

mary=Person("Mary", 30)
dave=Person("Dave", 40)
print(vars(mary))
print(type(vars(mary)["_age"]))
print("mary.age=",mary.age)   # 访问变量会触发getter，如果没加return返回值，就得到None
print(vars(dave))
mary.birthday()
print(dave.name)
print(dave.age)


# 软耦合
print("-------------------------------")
class LoggedAgeAccess1:
    def __set_name__(self,owner,name):
        self.public_name=name
        self.private_name="_"+name

    def __get__(self,obj, objtype=None):
        value=getattr(obj, self.private_name)
        print(f"Accessing {self.public_name !r} giving {value !r}")
        return value
    
    def __set__(self,obj,value):
        print(f"Updating {self.public_name !r} to {value !r}")
        setattr(obj,self.private_name,value)

class Person1:
    name=LoggedAgeAccess1()
    age=LoggedAgeAccess1()

    def __init__(self,name,age):
        print(111)
        self.name=name
        self.age=age
        print(222)
    
    def birthday(self):
        print(333)
        self.age += 1
        print(444)

print(vars(vars(Person1)["name"]))
print(vars(vars(Person1)["age"]))
print(vars(Person1))
pete=Person1("Peter",10)
kate=Person1("Catherine",20)
print(pete.age)
print(vars(pete))
print(vars(kate))


# 案例 验证器
class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name="_"+name
        print(self.private_name)
        print(333)
    
    def __get__(self,obj,objtype=None):
        print(444)
        return getattr(obj,self.private_name)
    
    def __set__(self,obj,value):
        print(555)
        self.validate(value)
        setattr(obj,self.private_name,value)
    
    @abstractmethod
    def validate(self,value):
        pass

class Oneof(Validator):
    def __init__(self,*options) -> None:
        self.options=set(options)
        print(options)
        print(111)
    
    def validate(self, value):
        print(222)
        print(value)
        if value not in self.options:
            raise ValueError(f"Expected {value !r} to be one of {self.options}")

class Component:
    kind=Oneof("wood","metal","plastic")

    def __init__(self,kind):
        self.kind=kind

c=Component("metle")
print(vars(c))
