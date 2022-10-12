# 1.----------------------------------------------
def f(x):
    return x*x

# 前后加双下划线表示系统定义的名字
# 有 A.py 和 B.py 两个文件，两个文件都有 "if __name__ == ……" 这样的结构，
# 此时将 A.py 导入 B.py，执行B.py，
# 在 A.py 中的 __name__ 的值就为 "A"，此时 A.py 中相应的代码块就不被执行，
# 而 B.py 中的 "if __name__ == ……" 结构下的代码被正常执行
if __name__=='__main__':
    r=map(f,[1,2,3,4,5,6,7,8,9])
    s=map(str,[1,2,3,4,5,6,7,8,9])
    print(type(r))
    print(type(s))
    print(list(r))
    print(list(s))


# 2.----------------------------------------------
from functools import reduce
def add(x,y):
    return x+y

if __name__=='__main__':
    result=reduce(add,[1,3,5,7,9])
    print(type(result))
    print(result)


# 3.----------------------------------------------
def fn(x,y):
    return x*10+y

def CharToInt(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    # return{}[]实际返回的是字典中key为s所对应的值

if __name__=='__main__':
    result=reduce(fn,map(CharToInt,'13579'))
    # print(list(map(CharToInt,'13579')))
    print(result)


# 4.----------------------------------------------
def is_odd(n):
    return n%2==1

def not_empty(s):
    return s and s.strip()

if __name__=='__main__':
    result=filter(is_odd,[1,2,4,5,6,9,10,15])
    print(type(result))
    print(list(result))
    print(list(filter(not_empty,['A','','B',None,'C','   '])))


# 5.----------------------------------------------
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

if __name__=='__main__':
    f=lazy_sum(1,3,5,7,9)
    print(type(f))
    print(f())


# 6.----------------------------------------------
def square(num):
    return num**2

items=[1,2,3,4]
# squared=list(map(square,items))
squared=list(map(lambda x: x**2, items))
print(squared)


# 7.----------------------------------------------
m=[1,2,3,4]
result=filter(lambda x:x%2==1, m)
print(type(result))