# 有 A 和 B 两种类型 的汤。一开始每种类型的汤有 n 毫升。有四种分配操作：

# 提供 100ml 的 汤A 和 0ml 的 汤B 。
# 提供 75ml 的 汤A 和 25ml 的 汤B 。
# 提供 50ml 的 汤A 和 50ml 的 汤B 。
# 提供 25ml 的 汤A 和 75ml 的 汤B 。
# 当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为 0.25 的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。

# 注意 不存在先分配 100 ml 汤B 的操作。

# 需要返回的值： 汤A 先分配完的概率 +  汤A和汤B 同时分配完的概率 / 2。返回值在正确答案 10-5 的范围内将被认为是正确的。


# ????
class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        print(n)
        if n >= 179:
            return 1.0
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        print(dp)
        dp[0] = [0.5] + [1.0] * n
        print(dp[0])
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] +
                            dp[max(0, i - 2)][max(0, j - 2)] + dp[max(0, i - 1)][max(0, j - 3)]) / 4
                print(dp)
        return dp[n][n]

S=Solution()
print(S.soupServings(50))
