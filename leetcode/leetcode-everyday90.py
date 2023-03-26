# 给你一个下标从 0 开始的整数数组 nums ，判断是否存在 两个 长度为 2 的子数组且它们的 和 相等。注意，这两个子数组起始位置的下标必须 不相同 。
# 如果这样的子数组存在，请返回 true，否则返回 false 。
# 子数组 是一个数组中一段连续非空的元素组成的序列。


class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        h={}
        for i in range(len(nums)-1):
            s=nums[i]+nums[i+1]
            a=h.get(s,-1)
            if a!=-1:
                return True
            else:
                h[s]=1
        return False