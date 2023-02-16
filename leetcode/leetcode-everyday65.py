# 给你一个下标从 0 开始的整数数组 nums 。在一步操作中，你可以执行以下步骤：
# 从 nums 选出 两个 相等的 整数
# 从 nums 中移除这两个整数，形成一个 数对
# 请你在 nums 上多次执行此操作直到无法继续执行。
# 返回一个下标从 0 开始、长度为 2 的整数数组 answer 作为答案，其中 answer[0] 是形成的数对数目，answer[1] 是对 nums 尽可能执行上述操作后剩下的整数数目。

from collections import Counter


class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        s=set(nums)
        cnt=Counter(nums)
        a=0
        b=0
        for i in s:
            a+=int(cnt[i]/2)
            if cnt[i]%2==1:
                b+=1
        return [a,b]