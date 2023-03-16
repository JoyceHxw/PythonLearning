# 给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。
# 统计并返回 nums 中的 中位数 等于 k 的非空子数组的数目。
# 注意：
# 数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
# 例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
# 子数组是数组中的一个连续部分。
from collections import Counter


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        # 由于题目保证 nums 中的整数互不相同，「k 是长为奇数的子数组的中位数」等价于「子数组中小于 k 的数的个数 == 大于 k 的数的个数」。
        # 这相当于「左侧小于 + 右侧小于 (+1)== 左侧大于 + 右侧大于」。
        # 变形得到「左侧小于 - 左侧大于 (+1)== 右侧大于 − 右侧小于」。  (偶数的话，个数相差1)
        # 为了方便计算，把这四类数字等价转换：
        # 左侧小于：在 k 左侧且比 k 小的视作 1；
        # 左侧大于：在 k 左侧且比 k 大的视作 −1；
        # 右侧大于：在 k 右侧且比 k 大的视作 1；
        # 右侧小于：在 k 右侧且比 k 小的视作 −1。
        # 此外，把 k 视作 0。
        # https://www.bilibili.com/video/BV1sD4y1e7pr/?t=12m40s&vd_source=8c263a538fbef6679d7a742077194839

        pos=nums.index(k)
        cnt=Counter()
        cnt[0]=1  # 自己
        c=0
        print("------右边")
        # 右边
        for i in range(pos+1, len(nums)):
            c+=1 if nums[i]>k else -1
            print("c=",c)
            cnt[c]+=1
        
        c=0
        ans=cnt[0]+cnt[1]
        print(cnt)
        print("------左边")
        # 左边
        for i in range(pos-1, -1, -1):
            c+=1 if nums[i]<k else -1
            print("c=",c)
            ans+=cnt[c]+cnt[c+1]  # 加上与另一边相等的和差1的

        return ans
    
S=Solution()
print(S.countSubarrays([3,2,1,4,5],4))
