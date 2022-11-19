# 如果仅实现了__get__,就是非数据描述符 non-data descriptor
# 同时实现了除__get__以外的__set__或__delete__方法,就是数据描述符 data descriptor
# 如果一个类的类属性设置为描述器,那么它被称为此描述器的owner属主

# 描述器方法何时被触发:
# 当属主类中对是描述器的类属性进行访问时(即类似b.x),__get__方法被触发
# 当属主类中对是描述器的实例属性通过'.'号赋值时,__set__方法被触发

# 代码二
# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')

#     def __get__(self,instance,owner):
#         print('A.__get__ {} {} {}'.format(self,instance,owner))

# class B:
#     x  = A()

#     def __init__(self):
#         print('B.init')
#         print('-' * 20)
#         print(B.x)
#         # print(B.x.a1)   # AttributeError B.x为None,None没有a1属性
#         print('*' * 20)

# b = B()
# print(b.x.a1)  # AttributeError B.x为None,None没有a1属性
# 调用B类的类属性,被A类__get__方法拦截,并返回值None

# 代码三
# class A:

#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')

#     def __get__(self,instance,owner):
#         print('A.__get__ {} {} {}'.format(self,instance,owner))
#         return self

# class B:
#     x  = A()

#     def __init__(self):
#         print('B.init')
#         print('-' * 20)
#         print(B.x)
#         # print(B.x.a1)
#         print('*' * 20)

# b = B()
# print(b.x)
# print(b.x.a1)

# 解决上例中的返回值为None,将A类的实例返回,可成功调用A实例的a1属性

# # 代码四

# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')

#     def __get__(self,instance,owner):
#         print('A.__get__ {} {} {}'.format(self,instance,owner))
#         return self

# class B:
#     x  = A()
#     print(x)

#     def __init__(self):
#         print('B.init')
#         # self.x = 100    #  实例调用x属性时,直接查实例自己的__dict__
#         self.x = A()      # 实例调用x属性时,不进入A类的__get__方法
#         print(self.x)
#         print('-' * 20)
#         print(B.x)    # __get__
#         print(B.x.a1)    # __get__
#         print('*' * 20)

# b = B()
# print(b.x)
# print(b.x.a1)
# # 总结: 不论是实例还是类,只要是访问了是描述器的类属性,
# # 都会被描述器的__get__方法拦截
# # 属性的访问顺序(本质)

# 代码五
class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A.init')

    def __get__(self,instance,owner):
        print('A.__get__ {} {} {}'.format(self,instance,owner))
        return self

    def __set__(self,instance,value):
        print('A.__set__ {} {} {}'.format(self,instance,value))

class B:
    x  = A()
    print(x)

    def __init__(self):
        print('B.init')
        self.x = 100
        #         self.x = A()   # 同上面100结果类似
        print(self.x)
# print('-' * 20)
# print(B.x)
# print(B.x.a1)
# print('*' * 20)

b = B()
# print(b.x)
# print(b.x.a1)
print(b.__dict__)
print(B.__dict__)
# 屏蔽A类的__set__方法,实例的__dict__为{'x': 100}
# 不屏蔽A类的__set__方法,实例的__dict__为{}
# __set__方法本质将实例的__dict__的属性名清空,从而达到数据描述器优先于查实例字典的假象