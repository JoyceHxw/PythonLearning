# 给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。

# MK 平均值 按照如下步骤计算：

# 如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。
# 从这个容器中删除最小的 k 个数和最大的 k 个数。
# 计算剩余元素的平均值，并 向下取整到最近的整数 。
# 请你实现 MKAverage 类：

# MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。
# void addElement(int num) 往数据流中插入一个新的元素 num 。
# int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。


# 超出时间限制
# class MKAverage:

#     def __init__(self, m: int, k: int):
#         self.m=m 
#         self.k=k
#         self.lst=[]
#         print("init...")


#     def addElement(self, num: int) -> None:
#         print("add...")
#         self.lst.append(num)


#     def calculateMKAverage(self) -> int:
#         print("cal...")
#         if self.m>len(self.lst):
#             return -1
#         else:
#             lst2=self.lst[len(self.lst)-self.m:]
#             lst2.sort()
#             lst2=lst2[self.k:self.m-self.k]
#             return int(sum(lst2)/len(lst2))

from collections import deque
from unittest.util import sorted_list_difference
from sortedcontainers import SortedList


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.s = 0
        self.q = deque()
        self.lo = sorted_list_difference()
        self.mid = SortedList()
        self.hi = SortedList()

    def addElement(self, num: int) -> None:
        if not self.lo or num <= self.lo[-1]:
            self.lo.add(num)
        elif not self.hi or num >= self.hi[0]:
            self.hi.add(num)
        else:
            self.mid.add(num)
            self.s += num
        self.q.append(num)
        if len(self.q) > self.m:
            x = self.q.popleft()
            if x in self.lo:
                self.lo.remove(x)
            elif x in self.hi:
                self.hi.remove(x)
            else:
                self.mid.remove(x)
                self.s -= x
        while len(self.lo) > self.k:
            x = self.lo.pop()
            self.mid.add(x)
            self.s += x
        while len(self.hi) > self.k:
            x = self.hi.pop(0)
            self.mid.add(x)
            self.s += x
        while len(self.lo) < self.k and self.mid:
            x = self.mid.pop(0)
            self.lo.add(x)
            self.s -= x
        while len(self.hi) < self.k and self.mid:
            x = self.mid.pop()
            self.hi.add(x)
            self.s -= x

    def calculateMKAverage(self) -> int:
        return -1 if len(self.q) < self.m else self.s // (self.m - 2 * self.k)
