# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

# 动态规划
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):  # 遍历之前元素
                if nums[j]<nums[i]:  # 筛选严格递增
                    dp[i]=max(dp[i],dp[j]+1)
                # print(dp)
        return max(dp)

S=Solution()
print(S.lengthOfLIS([10,9,2,5,3,7,101,18]))