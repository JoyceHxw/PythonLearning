# 给你两个非负整数数组 rowSum 和 colSum ，其中 rowSum[i] 是二维矩阵中第 i 行元素的和， colSum[j] 是第 j 列元素的和。换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。
# 请找到大小为 rowSum.length x colSum.length 的任意 非负整数 矩阵，且该矩阵满足 rowSum 和 colSum 的要求。
# 请你返回任意一个满足题目要求的二维矩阵，题目保证存在 至少一个 可行矩阵。

class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m=len(rowSum)
        n=len(colSum)
        matrix=[[0]*n for _ in range(m)]
        # for i, rs in enumerate(rowSum):
        #     for j, cs in enumerate(colSum):
        #         matrix[i][j] = x = min(rs, cs)
        #         print(x)
        #         rs -= x
        #         colSum[j] -= x
        # return matrix
        i = j = 0  # 从左上角出发
        while i < m and j < n:
            rs, cs = rowSum[i], colSum[j]
            if rs < cs:
                matrix[i][j] = rs  # 去掉第 i 行
                colSum[j] -= rs
                i += 1  # 往下走
            else:
                matrix[i][j] = cs  # 去掉第 j 列
                rowSum[i] -= cs
                j += 1  # 往右走
        return matrix
