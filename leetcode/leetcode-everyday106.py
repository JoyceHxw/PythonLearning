# 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。
# 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。

# 第一次自己做出来二维数组的dp
class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n=len(nums)
        ans=1
        # 二维数组，第一位为元素下标，第二位为差值
        # 表示前i位元素，差值为k的等差数列的个数
        # 差值为-500-500
        f=[[1]*1001 for _ in range(n)] 
        # print(f)
        for i in range(1,n):
            for j in range(0,i):
                k=nums[i]-nums[j]+500  # 使插值为正，与下标对应
                f[i][k]=max(f[i][k],f[j][k]+1)
                ans=max(ans,f[i][k])
        return ans