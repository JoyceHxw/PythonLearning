# 给定 m x n 矩阵 matrix 。
# 你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
# 返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        f={}
        # 即考察每一行的模式是否相同
        # 每一行分为以1开头和以0开头两种
        # 将以1开头的行进行翻转，然后用hash表存储模式一样的行
        for i in range(len(matrix)):
            if matrix[i][0]==1:
                for j in range(len(matrix[0])):
                    if matrix[i][j]==1:
                        matrix[i][j]=0
                    else:
                        matrix[i][j]=1
            # python 不能将可变值作为键，转换成tuple
            if f.get(tuple(matrix[i]),-1)==-1:
                f[tuple(matrix[i])]=1
            else:
                f[tuple(matrix[i])]+=1
        return max(f.values())