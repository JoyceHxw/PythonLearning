# 有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
# 每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
# 找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。

from cmath import inf
from itertools import accumulate

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        # 贪心算法 并不是全局最优解（[6,4,4,6])
        # ans=0
        # while len(stones)>=k:
        #     s={}
        #     min_sum=inf
        #     for i in range(0,len(stones)-k+1):
        #         a=0
        #         for j in range(i,i+k):
        #             a+=stones[j]
        #         s[a]=i
        #         min_sum=min(min_sum,a)
        #     m=s[min_sum]
        #     ans+=min_sum
        #     stone1=stones[:m]
        #     stone2=[min_sum]
        #     stone3=stones[m+k:]
        #     stones=stone1+stone2+stone3
        # if len(stones)==1:
        #     return ans
        # else:
        #     return -1


        # 动态规划
        # 对于 f[i][j][k]，我们可以枚举 i≤h<j，将区间 [i,j] 拆分成两个区间 [i,h] 和 [h+1,j]，
        # 然后将 [i,h] 中的石头合并成 1 堆，将 [h+1,j] 中的石头合并成 k−1 堆，
        # 最后将这两堆石头合并成一堆，这样就可以将区间 [i,j] 中的石头合并成 k 堆。
        # 因此，我们可以得到状态转移方程：f[i][j][k] = min{f[i][h][1] + f[h + 1][j][k - 1]}

        # n = len(stones)
        # if (n - 1) % (k - 1):
        #     return -1
        # s = list(accumulate(stones, initial=0))
        # f = [[[inf] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     f[i][i][1] = 0
        # for l in range(2, n + 1):
        #     for i in range(1, n - l + 2):
        #         j = i + l - 1
        #         for k in range(1, k + 1):
        #             for h in range(i, j):
        #                 f[i][j][k] = min(f[i][j][k], f[i][h][1] + f[h + 1][j][k - 1])
        #         f[i][j][1] = f[i][j][k] + s[j] - s[i - 1]
        # return f[1][n][1]


        n = len(stones)
        if (n - 1) % (k - 1):  # 无法合并成一堆
            return -1
        s = list(accumulate(stones, initial=0))  # 前缀和
        print(s)
        f = [[0] * n for _ in range(n)]
        print(f)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                print("i=",i)
                print("j=",j)
                f[i][j] = min(f[i][m] + f[m + 1][j] for m in range(i, j, k - 1))
                if (j - i) % (k - 1) == 0:  # 可以合并成一堆
                    f[i][j] += s[j + 1] - s[i]
                print(f)
        return f[0][-1]

S=Solution()
print(S.mergeStones([3,5,1,2,6],3))
