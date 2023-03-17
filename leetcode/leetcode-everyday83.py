# 给你一个长度为 n 的整数数组 nums ，和一个长度为 m 的整数数组 queries 。
# 返回一个长度为 m 的数组 answer ，其中 answer[i] 是 nums 中 元素之和小于等于 queries[i] 的 子序列 的 最大 长度  。
# 子序列 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。

# 注意queries不是按顺序排列的
from bisect import bisect_right
from itertools import accumulate


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # 两层循环，时间复杂度高
        # 先计算前缀和
        # nums.sort()
        # print(nums)
        # ans=[]
        # for q in queries:
        #     s=0
        #     cnt=0
        #     while s<=q and cnt<len(nums):
        #         s+=nums[cnt]
        #         cnt+=1
        #     if s<=q:
        #         cnt+=1
        #     print("s=",s)
        #     print("cnt=",cnt)
        #     ans.append(cnt-1)
        # return ans
    
        # 两次循环，时间复杂度地
        nums.sort()
        s = list(accumulate(nums))
        return [bisect_right(s, q) for q in queries]   # bisect.bisect和bisect.bisect_right返回大于x的第一个下标

S=Solution()
# print(S.answerQueries([4,5,2,1],[3,10,21]))  # [2,3,4]
# print(S.answerQueries([2,3,4,5],[1]))
print(S.answerQueries([736411,184882,914641,37925,214915],[331244,273144,118983,118252,305688,718089,665450]))  # [2,2,1,1,2,3,3]