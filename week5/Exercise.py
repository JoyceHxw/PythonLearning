# 1. 给定一个无序列表，列表中元素均为不重复的整数。请找出列表中有没有比它前面元素都大，比它后面的元素都小的数，
#   如果不存在则返回-1，存在则显示其索引，存在多个时只显示第一个解的索引
#   如果在第一位则算作比前面的都大，在最后一位则算作比后面都小。例如[1,2,3,4,5]中的1就是符合条件的第一个值。（索引为0）
print('\n','1----------------------------------------------------------------')
lst1=[6,3,4,9,1]
lst2=[4,3,6,9,7]
lst3=[1,3,2,4,5]

def middle(lst):
    is_flag1=True
    is_flag2=True
    for n in lst:
        if lst.index(n) == 0:
            is_flag1=True
            is_flag2=True
            for i in range(lst.index(n)+1,len(lst)):
                if n>=lst[i]:
                    is_flag2=False
                    continue
            if is_flag1==True and is_flag2==True:
                break
        elif lst.index(n) == len(lst)-1:
            is_flag1=True
            is_flag2=True
            for j in range(len(lst)-1):
                if n<=lst[j]:
                    is_flag1=False
                    continue
            if is_flag1==True and is_flag2==True:
                break
        else:
            is_flag1=True
            is_flag2=True
            for k in range(lst.index(n)):
                if n<=lst[k]:
                    is_flag1=False
                    continue
            for l in range(lst.index(n)+1,len(lst)):
                if n>=lst[l]:
                    is_flag2=False
                    continue
            if is_flag1==True and is_flag2==True:
                break

    if is_flag1==True and is_flag2==True:
        print(lst.index(n))
    else:
        print(-1)

middle(lst1)
middle(lst2)
middle(lst3)



# 2. 将list中的重复数据去重，至少使用两种方案。可以尝试结合其他数据结构。不要求保持原list顺序。
print('\n','2----------------------------------------------------------------')
lst4=[2,4,5,3,2,5,6,2,6]
def deduplicate(lst):
    for n in lst:
        if lst.count(n)>1:
            lst.remove(n)
        # print(lst)
    return lst

print(deduplicate(lst4))



# 3. 元组基本操作练习
# - 创建一个元组，分别进行索引、添加、长度计算、切片操作。
# 元组是不可以直接添加元素的，如果真的需要进行添加，可以使用什么样的方式实现？
# - 创建两个元组，进行连接操作。
# - 创建一个列表和元组，将其连接后打印出来。
print('\n','3----------------------------------------------------------------')
x=1,4,3,2,7,9,5,5,3,2,6  # 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
# 索引
print(x[4])
# 添加
x1=x+('joyce',)
print(x1)
# 长度
print(len(x1))
# 切片
print(x1[12:9:-1]) #从右向左切片
# 两个元组连接
x2=('zhao','qian','sun','li')
x3=x+x2
print(x3)
# 列表和元组连接
lst5=['huang','xuan','wen']
for n in x:
    lst5.append(n)
print(lst5)



# 4. 分别打印出以下集合的值，并说明原因。
print('\n','4----------------------------------------------------------------')
s1 = {32, 5,'c','32','11'}
s2 = set({32,'46',32,'aa'})
s3 = set('4,32,46,11,32')
s4 = set([1, 2, 3])              
s5 = set((1,2,3))
s6 = set({'a':1,'b':2,'c':3})
print(s1) #用{}创建集合
print(s2) #集合是无需的，不重复的元素序列，自动去重
print(s3) #将字符串看成列表，自动拆包
print(s4) #把序列转换成集合
print(s5) #把序列转换成集合
print(s6) #把字典转换成集合时，只会包含键



# 5. 有如下值集合[11,22,33,44,55,66,77,88,99,100,110,200,230,330]。
# 将所有大于66的值保存至字典的第一个key中，将等于小于66的值保存至第二个key中。 即：{‘k1’:大于66的值,‘k2’:小于等于66的值}
print('\n','5----------------------------------------------------------------')
s7=set([11,22,33,44,55,66,77,88,99,100,110,200,230,330])
lst6=[]
lst7=[]
for n in s7:
    if n>66:
        lst6.append(n)
    elif n<=66:
        lst7.append(n)

d1={'大于66的值':lst6, '小于等于66的值':lst7}
print(d1)



# 6. 以list1中的元素作为key，以list2中的元素作为value生成一个新的字典dict2。
print('\n','6----------------------------------------------------------------')
lst8=[1,2,3,4,5,6,7]
lst9=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
d2={}
for n in range(0,7):
    d2[lst8[n]]=lst9[n]
print(d2)



# 7.文本词频统计：：一篇文章，出现了哪些词？哪些词出现的最多？
# 请统计hamlet.txt文件中出现的英文单词情况，统计并输出出现最多的10个单词，以及出现的次数。注意：
# (1) 单词不区分大小写，即单词的大小写或组合形式一样；
# (2) 请在文本中剔除如下特殊符号：!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~
# （根据读取方式不同，可能还得忽略换行符）
# (3) 输出10个单词和它们的次数，每个单词和次数一行；
# (4) 输出单词为小写形式。
print('\n','7----------------------------------------------------------------')
# 读取txt文档
t=open('hamlet.txt',encoding='utf-8')
txt=t.read()
# 删除特殊字符
lst10=list('!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~')
# print(lst10)
for s in txt:
    if s in lst10:
        txt=txt.replace(s,'')
# 都转成小写
txt=txt.lower()
# print(txt)
# 将字符串转成列表
lst11=txt.split( )
# 去重，列出不同的单词
s8=set(lst11)
# 统计不同单词的重复出现的次数
d3={}
for w in s8:
    d3[w]=lst11.count(w)
# print(d3)
# 按照出现次数进行排序
lst12=sorted(d3.items(),key=lambda x:x[1],reverse=True)
# print(lst12)
# 选出前十个元素
for i in (range(0,10)):
    print(lst12[i])
# 关闭文档
t.close()