# 给你一个数组 seats 表示一排座位，其中 seats[i] = 1 代表有人坐在第 i 个座位上，seats[i] = 0 代表座位 i 上是空的（下标从 0 开始）。
# 至少有一个空座位，且至少有一人已经坐在座位上。
# 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
# 返回他到离他最近的人的最大距离。

class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        # 找最长连续空座位
        # 动态规划,找每个座位结尾的最长空座位
        dp=[0]*(len(seats))
        # 坐到边上
        edge=[]
        ans=0
        for i in range(len(seats)):
            if seats[i]==0:
                if i>0:
                    dp[i]=dp[i-1]+1
                else:
                    dp[i]=1
                ans=max(ans,dp[i])
                if dp[i]==i+1 or i==len(seats)-1:
                    edge.append(dp[i])
        max_edge=0 if edge==[] else max(edge)
        return max(int((ans+1)/2),max_edge)