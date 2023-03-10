# 给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
# 请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
# 子数组 定义为原数组中连续的一组元素。

# 前缀和，模定理
# 去掉的元素和和所有元素和同余
# s[right]−s[left]≡x(modp)移项得s[right]−x≡s[left](modp)

from itertools import accumulate


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        # 前缀和
        s = list(accumulate(nums, initial=0))
        x = s[-1] % p
        if x == 0: return 0  # 移除空子数组（这行可以不要）
        print(s)

        ans = n = len(nums)
        last = {}
        for i, v in enumerate(s):
            last[v % p] = i
            print(v-x)
            j = last.get((v - x) % p, -n)  # 如果不存在，-n 可以保证 i-j >= n
            print("j=",j)
            ans = min(ans, i - j)
        print(last)
        return ans if ans < n else -1

S=Solution()
S.minSubarray([6,3,5,2], 9)
