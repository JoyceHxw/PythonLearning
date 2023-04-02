# 你有一个凸的 n 边形，其每个顶点都有一个整数值。给定一个整数数组 values ，其中 values[i] 是第 i 个顶点的值（即 顺时针顺序 ）。
# 假设将多边形 剖分 为 n - 2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 n - 2 个三角形的值之和。
# 返回 多边形进行三角剖分后可以得到的最低分 。


# 动态规划
class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        # n*n的矩阵
        f = [[0] * n for _ in range(n)]
        print(f)
        # 枚举i到j的所有多边形f[i][j]
        # 从n-3开始，从n-3到n-1至少有一个三角形，从最少一个三角形开始
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                # i到j是确定的两个点，遍历其中的点，找到最小的划分从i到j多边形的值，利用已得到的三角形划分
                # 当i，j相邻时，不能构成三角形
                print("i=",i)
                print("j=",j)
                f[i][j] = min(f[i][k] + f[k][j] + values[i] * values[k] * values[j] for k in range(i + 1, j))
                print(f)
        return f[0][-1]
    
S=Solution()
print(S.minScoreTriangulation([1,3,1,4,1,5]))

