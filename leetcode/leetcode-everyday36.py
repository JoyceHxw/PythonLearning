# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

# nums.length == n
# nums[i] 是 正整数 ，其中 0 <= i < n
# abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
# nums 中所有元素之和不超过 maxSum
# nums[index] 的值被 最大化
# 返回你所构造的数组中的 nums[index] 。

# 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。



# 根据题目描述，如果我们确定了 nums[index] 的值为 x，此时我们可以找到一个最小的数组总和。
# 也就是说，在 index 左侧的数组元素从 x−1 每次递减 1，如果减到 1 后还有剩余元素，那么剩余的元素都为 1；
# 同样的，在 index 及右侧的数组元素从 x 也是每次递减 1，如果减到 1 后还有剩余元素，那么剩余的元素也都为 1。
# 这样我们就可以计算出数组的总和，如果总和小于等于 maxSum，那么此时的 x 是合法的。随着 x 的增大，数组的总和也会增大，因此我们可以使用二分查找的方法，找到一个最大的且符合条件的 x。
# 为了方便计算数组左侧、右侧的元素之和，我们定义一个函数 sum(x, cnt)sum(x,cnt)，表示一共有 cntcnt 个元素，且最大值为 xx 的数组的总和。函数 sum(x, cnt)sum(x,cnt) 可以分为两种情况：
# 如果 x ≥cnt，那么数组的总和为 (x+x−cnt+1)×cnt/2   (等差数列求和)
# 如果 x<cnt，那么数组的总和为 (x+1)×x/2​+cnt−x
# 接下来，定义二分的左边界 left = 1，右边界 right = maxSum，然后二分查找 nums[index] 的值 mid，如果 sum(mid - 1, index) + sum(mid, n - index)≤maxSum，那么此时的 midmid 是合法的，我们可以将 leftl更新为 mid，否则我们将 right 更新为 mid - 1。
# 最后将 left作为答案返回即可

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sum(x, cnt):
            return (x + x - cnt + 1) * cnt // 2 if x >= cnt else (x + 1) * x // 2 + cnt - x

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if sum(mid - 1, index) + sum(mid, n - index) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left
