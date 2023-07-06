# 给你一个整数 finalSum 。请你将它拆分成若干个 互不相同 的正偶数之和，且拆分出来的正偶数数目 最多 。
# 比方说，给你 finalSum = 12 ，那么这些拆分是 符合要求 的（互不相同的正偶数且和为 finalSum）：(2 + 10) ，(2 + 4 + 6) 和 (4 + 8) 。它们中，(2 + 4 + 6) 包含最多数目的整数。注意 finalSum 不能拆分成 (2 + 2 + 4 + 4) ，因为拆分出来的整数必须互不相同。
# 请你返回一个整数数组，表示将整数拆分成 最多 数目的正偶数数组。如果没有办法将 finalSum 进行拆分，请你返回一个 空 数组。你可以按 任意 顺序返回这些整数。

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        # ans=[]
        # if finalSum%2==1:
        #     return ans
        # # 有多少个2
        # n=finalSum/2
        # # 如何分配，贪心算法，先考虑1到i
        # i=1
        # while i*(i+1)/2<=n:
        #     i+=1
        # i-=1
        # # 剩余的从大到小加一，避免重复
        # r=n-i*(i+1)/2
        # j=i
        # c=1
        # while j>=1:
        #     k=1 if c<=r else 0
        #     ans.append(2*(j+k))
        #     j-=1
        #     c+=1
        # return ans

        # 优化：将前两步合并
        res = []
        if finalSum % 2 > 0:
            return res
        i = 2
        while i <= finalSum:
            res.append(i)
            finalSum -= i
            i += 2
        # 直接把剩余值加到最大的数上
        res[-1] += finalSum
        return res

        