# 如果一个正方形矩阵满足下述 全部 条件，则称之为一个 X 矩阵 ：
# 矩阵对角线上的所有元素都 不是 0
# 矩阵中所有其他元素都是 0
# 给你一个大小为 n x n 的二维整数数组 grid ，表示一个正方形矩阵。如果 grid 是一个 X 矩阵 ，返回 true ；否则，返回 false 。

class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        for i in range(len(grid)):
            if grid[i][i]==0 or grid[i][len(grid[i])-1-i]==0:
                return False
            for j in range(len(grid)):
                if j!=i and j!=len(grid[i])-1-i:
                    if grid[i][j]!=0:
                        return False
        return True