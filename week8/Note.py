# 类的继承
# 多继承遵循MRO算法（merge）（拓扑排序）：根据声明顺序查找，从左到右查找，菱形继承的极大值最后查找

# 使用类名调用父类方法的问题
class Base:
    def __init__(self) -> None:
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self) -> None:
        print("enter A")
        Base.__init__(self)
        print("leave A")

class B(Base):
    def __init__(self) -> None:
        print("enter B")
        Base.__init__(self)
        print("leave B")

class C(A,B):
    def __init__(self) -> None:
        print("enter C")
        A.__init__(self)
        B.__init__(self)
        print("leave C")

c=C()
# 会重复调用Base类（菱形继承）

print("super","-"*20)
# super()可以解决重复调用和查找顺序的问题
# A->B->Base
class Base1:
    def __init__(self) -> None:
        print("enter Base")
        print("leave Base")

class A1(Base1):
    def __init__(self) -> None:
        print("enter A")
        super().__init__()
        print("leave A")

class B1(Base1):
    def __init__(self) -> None:
        print("enter B")
        super().__init__()
        print("leave B")

class C1(A1,B1):
    def __init__(self) -> None:
        print("enter C")
        super().__init__()
        print("leave C")

c1=C1()


class A2:
    def test(self):
        print("A",self)

class B2:
    def test(self):
        print("B",self)

class C2(A2,B2):
    def __init__(self) -> None:
        super().test()  # 调用A类中的test方法
        super(C2,self).test()    # 调用A类中的test方法
        super(A2,self).test()    # 调用B类中的test方法

c2=C2()


# super中实例的指向
class Goat(object):
    def __init__(self) -> None:
        self.name='Jordan'
        print(f"{self.name}将篮球推向了全世界")
    
    def god_goat(self):
        print(f"{self.name}是历史上最伟大的篮球运动员")

class Mamba(Goat):
    def __init__(self) -> None:
        self.name='Kobe'
        print(f"{self.name}最具职业精神的篮球运动员")
        super().__init__()
        super().god_goat()
    
    def god_mamba(self):
        print(f"{self.name}是最喜欢的球员")

class KingJames(Mamba):
    def __init__(self) -> None:
        self.name='James'
        print(f"{self.name}最全能的篮球运动员")
    
    def god(self):
        print(f"{self.name}是FMVP运动员")
        super().__init__()
        super().god_mamba()

kj=KingJames()
kj.god()
# self都是实例kj，kj.name被修改
