# 给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。
# 注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。

from itertools import accumulate


class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        # 不相邻
        # nums.sort(reverse=True)
        # cnt=0
        # s=0
        # for n in nums:
        #     if cnt<k-1:
        #         s+=n
        #         print('n=',n)
        #         cnt+=1
        #     else:
        #         break
        # print(nums[cnt:])
        # s+=sum(nums[cnt:])/(len(nums)-cnt)
        # return s

# 平均值和最大的分组的子数组数目必定是 k。
# 为了方便计算子数组的平均值，我们使用一个数组 prefix 来保存数组 nums 的前缀和。我们使用 dp[i][j] 表示 nums 在区间 [0,i−1] 被切分成 j 个子数组的最大平均值和，显然 i≥j，计算分两种情况讨论：
# 当 j = 1 时，dp[i][j] 是对应区间 [0,i−1] 的平均值；
# 当 j > 1 时，我们将可以将区间 [0,i−1] 分成[0,x−1] 和 [x,i−1] 两个部分，其中 x≥j−1，那么 dp[i][j] 等于所有这些合法的切分方式的平均值和的最大值。
        n = len(nums)
        prefix = list(accumulate(nums, initial=0))
        print(prefix)
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        print(dp)
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i
        print(dp)
        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for x in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefix[i] - prefix[x]) / (i - x))
        return dp[n][k]


S=Solution()
print(S.largestSumOfAverages([4,1,7,5,6,2,3],4))