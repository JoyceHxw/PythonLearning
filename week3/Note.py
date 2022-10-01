# 注意函数与方法（对象）的区别：
# 函数名一般小写，用小驼峰（my_abs）
# 函数一般有返回值return，return之后的语句不会执行
# 自定义函数：1.定义函数时，要确定函数名和参数个数；
#       2.如果有必要，可以对参数的数据类型做检查；
#       3.函数执行完毕没有return语句时，自动return None（考试概念题）;
#       4.函数不可以同时返回多个值，但不报错，其实就是一个tuple，整体时一个值
# 集合set的元素必须唯一，可以用来去重


# 局部变量为组合数据类型且未创建，等同于全局变量
# 组合数据类型是用指针来体现的，所以函数中如果没有真实创建组合数据类型，它使用的变量是使用的指针，而指针指的是外部的全局变量
# 列表是可变的，直接作用于列表本身 （可变对象有：字典、列表、集合、自定义得对象）
def add_end(lst=[]):
    lst.append('END')
    return lst

print(add_end())
print(add_end())

# 对不可变对象进行操作，会产生一个新得对象空间，并用新得值填充这块空间 （不可变得对象有：数字、字符串、元组、function）
def add_end1(lst=None):
    if lst is None:
        lst=[]
        lst.append('END')
    return lst

print(add_end1())
print(add_end1())

def add_end2(num=1):
    num+=1
    return num

print(add_end2())
print(add_end2())


# 调用的时候，需要先组装出一个list或tuple
def calc(numbers):
    sum=0
    for n in numbers:
        sum+=n*n
    return sum

print(calc((1,2,3)))

# 可变参数（接收tuple）
def calc1(*numbers):
    sum=0
    for n in numbers:
        sum+=n*n
    return sum

nums=[1,2,3]
print(calc1(1,2,3))
print(calc1(nums[0],nums[1],nums[2]))
print(calc1(*nums))


# 关键字参数（接收dict）
# 关键字参数必须位于所有位置参数之后
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Michael',30)
person('Bob',35,city='Beijing') #调用函数时赋值相当于字典
person('Adam',45,gender='M',job='Engineer')
extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)

def person1(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

person1('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456) #仍可以传入不受限制的关键字参数

# 命名关键字参数（限制关键字参数的名字）
def person2(name,age,*,city,job):
    print('name:',name,'age:',age,'city:',city,'job:',job)

person2('Jack',24,city='Beijing',job='Engineer')

def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,3)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)

f2(1,2,d=99,ext=None)
f2(1,2,3,d=99,ext=None)

args=(1,2,3,4)
kw={'d':99,'x':'#'}

args1=(1,2,3)
kw1={'d':88,'x':'#'}
f1(*args,**kw)
f2(*args1,**kw1)