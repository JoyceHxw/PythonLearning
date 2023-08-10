# 给你一个 n x n 整数矩阵 grid ，请你返回 非零偏移下降路径 数字和的最小值。
# 非零偏移下降路径 定义为：从 grid 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。
 

# 应该再多想想，这道题的动态规划其实不难理解
class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        # 回溯
        # min_s=inf
        # def recursion(last,i,s):
        #     if i==len(grid):
        #         nonlocal min_s
        #         min_s=min(s,min_s)
        #         return
        #     for j in range(len(grid[0])):
        #         if j!=last:
        #             s+=grid[i][j]
        #             recursion(j,i+1,s)
        #             s-=grid[i][j]
        # recursion(-1,0,0)
        # return min_s

        # 动态规划
        # 二维数组保存选择该位置的路径最小值
        # n=len(grid)
        # d=[[10**9 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     d[0][i]=grid[0][i]
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if j==k:
        #                 continue;
        #             d[i][j]=min(d[i][j],d[i-1][k]+grid[i][j])
        # return min(d[n-1])

        # 优化，不需要遍历k，只需要保存两个上一行的最小值
        first_min_sum, second_min_sum = 0, 0
        first_min_index = -1
        for i in range(len(grid)):
            cur_first_min_sum, cur_second_min_sum = 10**9, 10**9
            cur_first_min_index = -1
            for j in range(len(grid)):
                cur_sum = grid[i][j]
                if j != first_min_index:
                    cur_sum += first_min_sum
                else:
                    cur_sum += second_min_sum
                if cur_sum < cur_first_min_sum:
                    cur_second_min_sum, cur_first_min_sum = cur_first_min_sum, cur_sum
                    cur_first_min_index = j
                elif cur_sum < cur_second_min_sum:
                    cur_second_min_sum = cur_sum
            first_min_sum, second_min_sum = cur_first_min_sum, cur_second_min_sum
            first_min_index = cur_first_min_index
        return first_min_sum
