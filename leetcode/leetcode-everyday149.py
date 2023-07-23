# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


# Hard往往可以较容易地想到暴力的方法，但是会超时
# 优化方法比较难想
class Solution:
    def trap(self, height: list[int]) -> int:
        # 暴力解法：对于每个height，遍历左右最大高度，减去当前height
        # ans=0
        # for i in range(1,len(height)-1):
        #     left_max=0
        #     for j in range(0,i+1):
        #         left_max=max(left_max,height[j])
        #     right_max=0
        #     for k in range(i,len(height)):
        #         right_max=max(right_max,height[k])
        #     ans+=min(left_max,right_max)-height[i]
        # return ans
        
        # 动态规划，遍历两边，保存左右两边的最大高度
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

            