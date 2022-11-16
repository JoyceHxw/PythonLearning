# 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
# 全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
# 0 <= i < j < n
# nums[i] > nums[j]
# 局部倒置 的数目等于满足下述条件的下标 i 的数目：
# 0 <= i < n - 1
# nums[i] > nums[i + 1]
# 当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。


class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        # num1=0
        # num2=0
        # for i in range(0,len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         num2+=1
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>nums[j]:
        #             num1+=1
        # return num1==num2


# 一个局部倒置一定是一个全局倒置，因此要判断数组中局部倒置的数量是否与全局倒置的数量相等，只需要检查有没有非局部倒置就可以了。
        min_suf = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i - 1] > min_suf:
                return False
            min_suf = min(min_suf, nums[i])
        return True
