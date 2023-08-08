# 给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。
# 请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。
# abs(x) 定义如下：
# 如果 x 是负整数，那么 abs(x) = -x 。
# 如果 x 是非负整数，那么 abs(x) = x 。

# 很明显的分类讨论
class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        # 连续最大和，连续最小和
        # 动态规划：要么加入上一个连续数组，要么自己重新开始
        last_max=0
        last_min=0
        max_sum=0
        min_sum=0
        for num in nums:
            last_max=max(last_max+num,num)
            max_sum=max(last_max,max_sum)
            last_min=min(last_min+num,num)
            min_sum=min(last_min,min_sum)
        return max(max_sum,-min_sum)
