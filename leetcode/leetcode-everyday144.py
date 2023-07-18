# 给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示第 i 个区间开始于 lefti 、结束于 righti（包含两侧取值，闭区间）。区间的 长度 定义为区间中包含的整数数目，更正式地表达是 righti - lefti + 1 。
# 再给你一个整数数组 queries 。第 j 个查询的答案是满足 lefti <= queries[j] <= righti 的 长度最小区间 i 的长度 。如果不存在这样的区间，那么答案是 -1 。
# 以数组形式返回对应查询的所有答案。

from heapq import heappop, heappush


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # 暴力
        # ans=[]
        # for j in range(len(queries)):
        #     min_dis=inf
        #     for i in range(len(intervals)):
        #         if intervals[i][0]<=queries[j]<=intervals[i][1]:
        #             min_dis=min(min_dis,intervals[i][1]-intervals[i][0]+1)
        #     min_dis=-1 if min_dis==inf else min_dis
        #     ans.append(min_dis)
        # return ans
        
        # 答案：优先队列+最小堆
        qindex = list(range(len(queries)))
        # 搜索值从小到大排序
        qindex.sort(key=lambda i: queries[i])
        # 区间按left从大到小排序
        intervals.sort(key=lambda i: i[0])
        pq = []
        res = [-1] * len(queries)
        i = 0
        # 从最小值遍历最小区间
        for qi in qindex:
            while i < len(intervals) and intervals[i][0] <= queries[qi]:
                # 加入最小堆
                heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            # right<query，剔除，由于后续元素更大，所以可以剔除
            while pq and pq[0][2] < queries[qi]:
                heappop(pq)
            # 第一个满足条件的即为长度最小区间
            if pq:
                res[qi] = pq[0][0]
        return res
