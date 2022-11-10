class Base1:
    def f1(self):
        print('base1.f1')
    
    def f2(self):
        print('base1.f2')
    
    def f3(self):
        print('base1.f3')

class Base2:
    def f1(self):
        print('base2.f1')

class Foo(Base1,Base2):
    def f0(self):
        print('foo.f0')
        self.f3()

obj=Foo()
obj.f0()



print("------------------------------------")
class Base3:
    def f1(self):
        print('base.f1')
    
    def f3(self):
        self.f1()
        print('base.f3')

class Foo1(Base3):
    def f1(self):
        print('foo.f1')
    
    def f2(self):
        print('foo.f2')
        self.f3()

obj2=Base3()
# obj2.f2()



print("------------------------------------")
class Base4:
    def __init__(self) -> None:
        print('执行Base.__init')
        self.func()
    
    def func(self):
        print('Base.func')

class Foo2:
    def __init__(self) -> None:
        print('执行Foo.__init')
        # self.func()

        # def func(self):
        #     print('Foo.func')

f=Foo2()



print("------------------------------------")
class A(object):
    @classmethod
    def f1(cls):
        print(cls)
    
    def f2(self):
        self.f1()
        A.f1()

obj3=A()
obj3.f2()



print("------------------------------------")
class A1(object):
    a=11

    def __init__(self,num) -> None:
        self.b=num

obj4=A1(123)
print(obj4.a)
print(obj4.b)

print(A1.a)
# print(A1.b)



print("------------------------------------")
class A2(object):
    a1=1

    def __init__(self,num) -> None:
        self.b1=num

obj5=A2(123)
obj6=A2(555)
print(obj5.b1)
print(obj5.a1)

obj5.b1=13
obj5.a1=22

print(obj5.b1)
print(obj5.a1)

print(obj6.a1)
print(obj6.b1+A2.a1)
print(obj6.b1+obj5.a1)



print("------------------------------------")
class A3(object):
    @classmethod
    def f(cls):
        print(cls)

A3.f()

obj7=A3()
obj7.f()



print("------------------------------------")
class StarkConfig(object):
    def __init__(self,num) -> None:
        self.num=num
    
    def changelist(self,request):
        print(self.num,request)
    
    def run(self):
        self.changelist(999)

class RoleConfig(StarkConfig):
    def changelist(self, request):
        print(777,self.num)

config_obj_list=[StarkConfig(1),StarkConfig(2),StarkConfig(3)]
config_obj_list[1].run()
config_obj_list[2].run()