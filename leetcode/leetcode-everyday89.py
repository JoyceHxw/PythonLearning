# 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
# 一个子数组指的是原数组中连续的一个子序列。
# 请你返回满足题目要求的最短子数组的长度。

from bisect import bisect_left

# 双指针 + 二分查找
# 我们先找出数组的最长非递减前缀和最长非递减后缀，分别记为 nums[0..i] 和 nums[j..n−1]。
# 如果 i≥j，说明数组本身就是非递减的，返回 0。
# 否则，我们可以选择删除右侧后缀，也可以选择删除左侧前缀

class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        i, j = 0, n - 1
        while i + 1 < n and arr[i] <= arr[i + 1]:
            i += 1
        while j - 1 >= 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if i >= j:
            return 0
        ans = min(n - i - 1, j)
        print("i=",i)
        print("j=",j)
        print(ans)
        for l in range(i + 1):
            print("l=",l)
            r = bisect_left(arr, arr[l], lo=j)  # bisect_left返回大于等于x的第一个下标 lo是检索的起始位置
            print("r=",r)
            # 删除 nums[l+1..r−1]
            ans = min(ans, r - l - 1)
        return ans

S=Solution()
print(S.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))