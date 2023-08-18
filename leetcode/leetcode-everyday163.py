# 给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：
# 你挑选 任意 一块披萨。
# Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
# Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
# 重复上述过程直到没有披萨剩下。
# 每一块披萨的大小按顺时针方向由循环数组 slices 表示。
# 请你返回你可以获得的披萨大小总和的最大值。


# 基本思路与打家劫舍类似，但是切入点3n很难想到
class Solution:
    def maxSizeSlices(self, slices: list[int]) -> int:
        # 感觉类似于环形打家劫舍，不能相邻
        # 分类讨论是否选择第一个元素
        # 区别在于，披萨会被拿掉，相邻元素变化，所以只考虑不相邻还不够
        # 转化为在长度为3n的换装序列种，选择n个不相邻的数（一定存在一个数的某一侧有连续两个数没有被选择），变成二维动态规划
        def sub(slices):
            N=len(slices)
            n=(len(slices)+1)//3
            # dp[i][j]为前i个数种选择j个不相邻的数的最大和
            dp=[[-10**9 for i in range(n+1)] for j in range(N)]
            dp[0][0]=0
            dp[0][1]=slices[0]
            dp[1][0]=0
            dp[1][1]=max(slices[0],slices[1])
            for i in range(2,N,1):
                dp[i][0]=0
                for j in range(1,n+1,1):
                    dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+slices[i])
            return dp[N-1][n]
        a1=sub(slices[1:])
        a2=sub(slices[0:-1])
        return max(a1,a2)