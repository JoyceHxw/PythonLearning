# 给你一个整数数组 nums 和两个整数：left 及 right 。
# 找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。


# 一个子数组的最大值范围在[left,right] 表示子数组中不能含有大于right 的元素，且至少含有一个处于 [left,right] 区间的元素。
# 我们可以将数组中的元素分为三类，并分别用 0, 1, 2 来表示：
# 小于left，用 0 表示；
# 大于等于 left 且小于等于 right，用 1 表示；
# 大于 right，用 2 表示。
# 那么本题可以转换为求解不包含 2，且至少包含一个 1 的子数组数目。我们遍历 i，并将右端点固定在 i，求解有多少合法的子区间。过程中需要维护两个变量：
# last1，表示上一次 1 出现的位置，如果不存在则为 -1；
# last2​，表示上一次 2 出现的位置，如果不存在则为 −1。

class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        res = 0
        last2 = last1 = -1
        for i, x in enumerate(nums):
            print(i,x)
            if left <= x <= right:
                last1 = i
            elif x > right:
                last2 = i
                last1 = -1
            print("last1=",last1)
            print("last2=",last2)
            if last1 != -1:
                res += last1 - last2
                print("res=",res)
        return res

S=Solution()
S.numSubarrayBoundedMax([2,9,2,5,6],2,8)