# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。


# 较简单的动态规划
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        # 递归超出时间限制
        # 动态规划
        n=len(matrix)
        f=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==0:
                    f[i][j]=matrix[i][j]
                else:
                    num1=10000
                    num3=10000
                    if j>0:
                        num1=f[i-1][j-1]
                    if j<n-1:
                        num3=f[i-1][j+1]
                    num2=f[i-1][j]
                    f[i][j]=min(num1+matrix[i][j],num2+matrix[i][j],num3+matrix[i][j])
        return min(f[n-1])