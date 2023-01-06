# 给你一个正整数 num ，请你统计并返回 小于或等于 num 且各位数字之和为 偶数 的正整数的数目。
# 正整数的 各位数字之和 是其所有位上的对应数字相加的结果。


class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            s=0
            for j in str(i):
                s+=int(j)
            if s%2==0:
                c+=1
        return c