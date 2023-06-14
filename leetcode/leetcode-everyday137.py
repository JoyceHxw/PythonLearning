# 给你一个长度为 n 、下标从 1 开始的二进制字符串，所有位最开始都是 0 。我们会按步翻转该二进制字符串的所有位（即，将 0 变为 1）。
# 给你一个下标从 1 开始的整数数组 flips ，其中 flips[i] 表示对应下标 i 的位将会在第 i 步翻转。
# 二进制字符串 前缀一致 需满足：在第 i 步之后，在 闭 区间 [1, i] 内的所有位都是 1 ，而其他位都是 0 。
# 返回二进制字符串在翻转过程中 前缀一致 的次数。

class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        # 前缀和，超出时间限制
        # s=[0]*(len(flips)+1)
        # cnt=0
        # step=0
        # for i in flips:
        #     k=i
        #     step+=1
        #     while k<=len(flips):
        #         s[k]+=1
        #         k+=1
        #     if s[step]==step:
        #         cnt+=1
        # return cnt

        # 维护翻转的最大值
        ans = right = 0
        for i, flip in enumerate(flips):
            right = max(right, flips[i])
            if right == i + 1:
                ans += 1
        return ans
