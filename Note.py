# list方法区分
# 一、list.remove(obj)
nums=[1,2,2,2,3,4,2]

for num in nums:
    print(num)
    if num == 2:
        nums.remove(2)
    print(nums)

print(nums)
# remove函数只去除列表中第一个找到的目标值
# 每次去除掉列表中的元素后，列表自动缩减，对应的索引值-1，所以会漏掉元素3

# 二、sorted() vs sort()
# sorted()会生成一个新的列表，不改变原来列表；sort()直接改变原列表
# sorted()可以对所有对象进行排序操作，sort()只能对列表操作
# reverse=True是逆序，reverse=False是升序

list1=[5,7,3,1,2,9]
list1.sort(reverse=True)
print(list1)

list2=[5,7,3,1,2,9]
sorted(list2,reverse=True)
print(list2)

list3=[("A",22),("B",17),("C",13),("D",24)]
list3.sort(key=lambda x:x[1],reverse=True)
print(list3)

# 三、reversed() vs reverse()
# 同二
list4=[5,7,3,1,2,9]
list4.reverse()
print(list4)

# 四、reverse() vs list[::-1]
# list[p1:p2:p3]
# p1，相当于start_index，可以为空，默认是0
# p2，相当于end_index，可以为空，默认是list.size
# p3，步长，默认为1。步长为-1时，返回倒序原序列
# list.reverse()没有返回值
list5=[5,7,3,1,2,9]
print(list5[0:4:2])
print(list5[::-1])
print(list5)

list6=[5,7,3,1,2,9]
print(list6.reverse())
