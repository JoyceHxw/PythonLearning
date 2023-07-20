# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。

# 这道题有一些技巧点：分类讨论，动态规划，前缀和，后缀和
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # 非环
        # ans=nums[0]
        # last=0
        # for n in nums:
        #     last=max(last+n,n)
        #     ans=max(ans,last)
        # return ans
        
        # 环：把列表拼接在后面
        # 暴力遍历：超出时间限制
        # n=len(nums)
        # for i in range(n-1):
        #     nums.append(nums[i])
        # ans=nums[0]
        # last=[0]*n
        # # 开头
        # for i in range(n):
        #     # 结尾
        #     for j in range(n):
        #         last[i]=max(last[i]+nums[i+j],nums[i+j])
        #         ans=max(last[i],ans)
        # return ans

        # 分两种情况：不跨界和跨界（前缀+后缀）
        n=len(nums)
        # 最大前缀和：要么是之前的前缀和，要么所有数求和
        leftMax=[0]*n
        leftMax[0]=nums[0]
        last=nums[0]
        ans=nums[0]
        s=nums[0]
        # 不跨界的情况
        for i in range(1,n):
            last=max(last+nums[i],nums[i])
            ans=max(last,ans)
            s+=nums[i]
            leftMax[i]=max(leftMax[i-1],s)
        # 跨界的情况：枚举后缀和的分界点
        # 从右到左枚举，顺便求出后缀和
        rightSum=0
        for i in range(n-1,0,-1):
            rightSum+=nums[i]
            ans=max(ans,leftMax[i-1]+rightSum)
        return ans