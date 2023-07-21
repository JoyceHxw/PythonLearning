# 给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。
# 请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.length。
# 题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。

from cmath import inf
from heapq import heappop, heappush


class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        # 暴力
        # ans=-inf
        # n=len(points)
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         temp=abs(points[i][0]-points[j][0])
        #         if temp<=k:
        #             ans=max(ans,points[i][1]+points[j][1]+temp)
        # return ans
        
        # 利用按横坐标排序，当i<j，yi + yj + |xi - xj|转化为xj+yj+yi-xi
        # yi-xi最大即为xi-yi最小
        # 最小堆
        res = -inf
        heap = []
        for x, y in points:
            while heap and x - heap[0][1] > k:
                heappop(heap)
            if heap:
                res = max(res, x + y - heap[0][0])
            heappush(heap, [x - y, x])
        return res
