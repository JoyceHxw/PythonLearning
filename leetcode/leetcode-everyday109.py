# 给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，长度分别为 firstLen 和 secondLen 。
# 长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。
# 子数组是数组的一个 连续 部分。


from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        # 前缀和
        s=list(accumulate(nums,initial=0))
        ans=s[firstLen+secondLen]
        # 假设在first在second左边
        a=s[firstLen]
        for i in range(firstLen+secondLen, len(s)): # second数组的右端点
            a=max(a,s[i-secondLen]-s[i-secondLen-firstLen])
            ans=max(ans,s[i]-s[i-secondLen]+a)
        # 假设first在second右边
        b=s[secondLen]
        # print(s)
        for j in range(firstLen+secondLen,len(s)):
            b=max(b,s[j-firstLen]-s[j-firstLen-secondLen])
            ans=max(ans,s[j]-s[j-firstLen]+b)
        return ans
