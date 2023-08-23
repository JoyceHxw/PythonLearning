# 给你一个无向图，无向图由整数 n  ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条无向边。同时给你一个代表查询的整数数组 queries 。
# 第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：
# a < b
# cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
# 请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答案。
# 请注意，图中可能会有 重复边 。

from bisect import bisect_right
import collections


class Solution:
    def countPairs(self, n: int, edges: list[list[int]], queries: list[int]) -> list[int]:
        # # 构建邻接矩阵
        # matrix=[[0]*(n+1) for i in range(n+1)]
        # for a,b in edges:
        #     matrix[a][b]+=1
        #     matrix[b][a]+=1
        # # print(matrix)
        # # 统计每个点的度
        # edge_nums=[0]*(n+1)
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         if matrix[i][j]>0:
        #             edge_nums[i]+=matrix[i][j]
        # # print(edge_nums)
        # # 遍历点对
        # lst=[]
        # for i in range(1,n+1):
        #     for j in range(i+1,n+1):
        #         lst.append(edge_nums[i]+edge_nums[j]-matrix[i][j])
        # # print(lst)

        # 优化，不用邻接矩阵
        edge_nums=[0]*n
        cnt = collections.defaultdict(int)
        for a,b in edges:
            # 为了用a*n+b统计两点之间的边的数量
            if a > b:
                a, b = b, a
            edge_nums[a-1]+=1
            edge_nums[b-1]+=1
            cnt[(a-1)*n+b-1]+=1
        print(cnt)

        # 遍历点对
        # lst=[]
        # for i in range(1,n+1):
        #     for j in range(i+1,n+1):
        #         lst.append(edge_nums[i]+edge_nums[j]-cnt[i*n+j])
        # # 统计满足条件的个数
        # lst.sort()
        # # print(lst)
        # ans=[]
        # # print(lst)
        # for k in queries:
        #     # 二分查找
        #     # left=0
        #     # right=len(lst)-1
        #     # while left<=right:
        #     #     mid=(left+right)//2
        #     #     if lst[mid]>k:
        #     #         right=mid-1
        #     #     else:
        #     #         left=mid+1
        #     ans.append(len(lst)-bisect_right(lst,k))
        # return ans

        # 优化，二分查找queries[i]−degree[b]
        arr = sorted(edge_nums)
        ans = []
        for bound in queries:
            total = 0
            for i in range(n):
                j = bisect_right(arr, bound - arr[i], i + 1)
                total += n - j
            # 考虑两点之间的边
            for val, freq in cnt.items():
                x, y = (val // n), (val % n)
                if edge_nums[x] + edge_nums[y] > bound and edge_nums[x] + edge_nums[y] - freq <= bound:
                    total -= 1
            ans.append(total)
        return ans
