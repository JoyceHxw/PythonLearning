# 1. 设计一个类Point表示点的坐标，有x和y两个属性表示横纵坐标。
# 要求通过重载运算符实现两个Point对象可以通过'+'相加
# 要求通过重载运算符实现两个Point对象可以通过'-'相减
from abc import abstractmethod


class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    
    def __add__(self,point):
        a=(self.x+point.x,self.y+point.y)
        return a
    
    def __sub__(self,point):
        s=(self.x-point.x,self.y-point.y)
        return s

p1=Point(2,3)
p2=Point(-1,2)
print(p1+p2)
print(p1-p2)


# 2. 写出以下代码运行结果并说明理由
class Parent:
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Child2.x = 3
print(Parent.x, Child1.x, Child2.x)


# 3. 先定义一个温度类，然后定义两个描述符类用于描述摄氏度和华氏度两个属性。可以给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果。
# 摄氏度类
class Celsius:
    def __init__(self, value=26.0):
        self.value = float(value)  

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

# 华氏度类
class Fahrnheit:
    def __get__(self, instance, owner):
        v=round(instance.cel*1.8+32,2)
        return v

    def __set__(self, instance, value):
        print("value=",32+value*1.8)
        instance.cel=32+value*1.8

# 描述符类
class Temperature:
    cel = Celsius() 
    f = Fahrnheit() 

    def __init__(self,cel) -> None:
        self.cel=cel


temp = Temperature(36.3)  # temp为描述符类实例
print(temp.cel)  # 可以查看摄氏度的值
print(temp.f)  # 并且可以直接计算出华氏度
temp.cel = 37.8  # 设置摄氏度的值
print(temp.f)  # 依据该值可计算出华氏度


# 4
class Des(object):
    def __init__(self, init_value) -> None:
        self.value=init_value
    
    def __get__(self,instance,typ):
        print('call __get__', instance, typ)
        return self.value
    
    def __set__(self,instance,value):
        print('call __set__', instance, value)
        self.value=value
    
    def __delete__(self, instance):
        print('call __delete__', instance)

class Widget(object):
    t=Des(1)

def main():
    w=Widget()
    # print(111)
    print(type(w.t))
    # print(222)
    w.t=1
    # print(333)
    print(w.t, Widget.t)
    # print(444)
    del w.t
    # print(555)

if __name__=='__main__':
    main()
