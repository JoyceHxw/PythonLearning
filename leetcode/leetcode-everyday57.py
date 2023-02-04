# 给你一个长度为 n 的整数数组 coins ，它代表你拥有的 n 个硬币。第 i 个硬币的值为 coins[i] 。如果你从这些硬币中选出一部分硬币，它们的和为 x ，那么称，你可以 构造 出 x 。
# 请返回从 0 开始（包括 0 ），你最多能 构造 出多少个连续整数。
# 你可能有多个相同值的硬币。


# 排列之后取数，如果可以前n个数得到连续x个整数，说明前x个数都可以构造得到，那么当下一个数y小于等于x时，一定可以构造得到x+y
class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        coins.sort()
        s=0
        for c in coins:
            if c<=s+1:
                s+=c
            else:
                return s+1
        return s+1

S=Solution()
print(S.getMaximumConsecutive([1,1,1,4]))