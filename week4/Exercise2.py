from functools import reduce
import math
#  1.fliter, reduce  求素数及其和
print('------------1.fliter, reduce求素数及其和--------------') 
def is_prime(r):
    is_flag=True
    if r==1:
        is_flag=False
    else:
        for i in range(2,int(math.sqrt(r))+1):
            if r%i == 0:
                is_flag=False
                break
    
    return is_flag

lst=list(range(1,101))
# result1=filter(is_prime,lst)
result1=filter(lambda x: not [x%i for i in range(2,int(math.sqrt(x))+1) if x%i==0] and x!=1,lst)
lst2=list(result1)
print(lst2)
result2=reduce(lambda a,b: a+b,lst2)
print(result2)

#  2.使用map()函数将用户姓名列表转换为规范形式：首字母大写，其他字母小写。
print('\n','------------2.使用map()函数将用户姓名列表转换为规范形式：首字母大写，其他字母小写。--------------')
lst3=['lisa','JACK','Adam']
print(lst3)
lst4=map(lambda x: x[0].upper() + x[1:].lower(),lst3)
print(list(lst4))

# 3.sorted按照排名对list进行排序
print('\n','------------3.sorted按照排名对list进行排序--------------')
lst5=[(1,'byd'),(3,'xiaopeng'),(2,'tesla'),(4,'weilai')]
print(lst5)
lst6=sorted(lst5,key=lambda x:x[0])
print(lst6)

# 4.使用闭包实现步数记录
print('\n','------------4.使用闭包实现步数记录--------------')
#闭包函数定义
def count_steps(original_step=0):

    def wrapper(new_steps):
        nonlocal original_step
        original_step = new_steps + original_step
        return original_step
            
    return wrapper
        
#执行语句
count_steps = count_steps(10)
print(count_steps(5))
print(count_steps(5))
print(count_steps(8))