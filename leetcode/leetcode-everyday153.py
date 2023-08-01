# 给你一个下标从 0 开始的整数数组 nums ，它表示英雄的能力值。如果我们选出一部分英雄，这组英雄的 力量 定义为：
# i0 ，i1 ，... ik 表示这组英雄在数组中的下标。那么这组英雄的力量为 max(nums[i0],nums[i1] ... nums[ik])2 * min(nums[i0],nums[i1] ... nums[ik]) 。
# 请你返回所有可能的 非空 英雄组的 力量 之和。由于答案可能非常大，请你将结果对 109 + 7 取余。

class Solution:
    def sumOfPower(self, nums: list[int]) -> int:
        # 回溯超出时间限制
        # combination=[]
        # ans=0
        # def recursion(k):
        #     if combination!=[]:
        #         max_num=max(combination)
        #         min_num=min(combination)
        #         nonlocal ans
        #         ans+=int(max_num*max_num*min_num % (10e9+7))
        #     for i in range(k,len(nums)):
        #         combination.append(nums[i])
        #         recursion(i+1)
        #         combination.pop()
        # recursion(0) 
        # return ans 

        # 分析题目：最大值/最小值，考虑排序，当最大值相同时，和为最大值的平方×最小值的和
        # 动态规划+前缀和
        nums.sort()
        dp=0
        pre_sum=0
        ans=0
        for i in range(len(nums)):
            dp=(nums[i]+pre_sum)%(10**9+7)
            pre_sum=(pre_sum+dp)%(10**9+7)
            ans=(ans+nums[i]*nums[i]*dp)%(10**9+7)
        return ans
