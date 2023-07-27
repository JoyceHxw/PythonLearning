# 给你一个 m x n 大小的矩阵 grid ，由若干正整数组成。
# 执行下述操作，直到 grid 变为空矩阵：
# 从每一行删除值最大的元素。如果存在多个这样的值，删除其中任何一个。
# 将删除元素中的最大值与答案相加。
# 注意 每执行一次操作，矩阵中列的数据就会减 1 。
# 返回执行上述操作后的答案。

class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        # 时间复杂度为n*n*m，空间复杂度为m*n
        # visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        # ans=0
        # for j in range(len(grid[0])):
        #     max_max_num=0
        #     for i in range(len(grid)):
        #         max_num=0
        #         max_index=0
        #         for k in range(len(grid[0])):
        #             if visited[i][k]==0 and grid[i][k]>max_num:
        #                 max_num=grid[i][k]
        #                 max_index=k
        #         # print(max_num)
        #         visited[i][max_index]=1
        #         max_max_num=max(max_max_num,max_num)
        #     ans+=max_max_num
        # return ans

        # 优化：排序
        # 时间复杂度为m*n*logn
        for i in range(len(grid)):
            grid[i].sort()
        ans=0
        for j in range(len(grid[0])):
            max_num=0
            for k in range(len(grid)):
                max_num=max(max_num,grid[k][j])
            ans+=max_num
        return ans