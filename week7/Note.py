class Student:
    university='Nankai University'   #类中的属性

    def __init__(self,name,school):   #类似于Java的构造器
        self.name=name
        self.school=school
    
    def take_class(self):   #类中的方法
        print(f"{self.name} is having {self.school}'s class...")


gj=Student("Guo Jing","G School")
hr=Student("Huang Rong","T School")

# 实例能访问类的属性，但类不能访问实例的属性，类调方法要传实例
# 实例查找修改属性先从实例里找，再从类里找
gj.take_class()  #实例化对象
hr.take_class()

gj.skill='Jiuyin Shengong'

print(gj.__dict__)
print(hr.__dict__)



# 类方法：有classmethod装饰的函数,类和实例都可以访问
# 实例方法：没有任何装饰器,有默认self的普通函数,实例访问
# 静态方法：有staticmethod装饰，没有参数的函数,类和实例都可以访问
class Person:
    unit="南开大学"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self,major):
        print(f"在下{self.name}，学的一手好{major}")

    @classmethod
    def sing(cls, song):
        print(f"在下{cls.unit}弟子，唱的一首好{song}")
        # 不可以传self

    @staticmethod
    def jump():
        print("在下Person类静态方法")

xww=Person("霹雳小汪汪",18)
xww.skill="Java"
xww.say("编程") 
xww.sing("《明天我依然爱你》")
Person.sing("《Hello》")   
xww.jump()
Person.jump() 



# 方法与函数的区别
# 普通函数（未定义在类里）和静态方法，都是函数
# 实例方法和类方法，都是方法
# 可以用type函数验证
print(type(xww.jump))
print(type(xww.sing))


# 双前导下划线
# __var:私有属性,不能再类外部被使用或直接访问,在类内部的方法中使用时:self.private_attrs
class Person1:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    
    def is_adult(self):
        return self.__age>=18

xh=Person1("小红",27)
print(xh.is_adult())
xh.__age=17  #相当于新建了一个属性,不改变原私有属性
print(xh.__age)
print(xh.__dict__)


class JustCounter:
    __secretCount=0
    publicCount=0

    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print(self.__secretCount)

counter=JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter._JustCount__secretCount)


# __method()私有方法,只能在类的内部调用: self.__private_method
class Site:
    def __init__(self,name,url) -> None:
        self.name=name
        self.__url=url
    
    def who(self):
        print('name: ', self.name)
        print('url: ', self.__url)
    
    def __foo(self):
        print("this is private method")
    
    def foo(self):
        print("this is public method")
        self.__foo()

x=Site('封装','www.yahoo.com')
x.who()
x.foo()
# x.__foo()

# 外部可以通过_类名__属性名/方法名来访问类中的私有属性/方法
x._Site__foo()
print(counter._JustCounter__secretCount)