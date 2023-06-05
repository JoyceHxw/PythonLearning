# 给你一个下标从 0 开始的数组 nums ，数组大小为 n ，且由 非负 整数组成。
# 你需要对数组执行 n - 1 步操作，其中第 i 步操作（从 0 开始计数）要求对 nums 中第 i 个元素执行下述指令：
# 如果 nums[i] == nums[i + 1] ，则 nums[i] 的值变成原来的 2 倍，nums[i + 1] 的值变成 0 。否则，跳过这步操作。
# 在执行完 全部 操作后，将所有 0 移动 到数组的 末尾 。
# 例如，数组 [1,0,2,0,0,1] 将所有 0 移动到末尾后变为 [1,2,1,0,0,0] 。
# 返回结果数组。
# 注意 操作应当 依次有序 执行，而不是一次性全部执行。


# 注意移动0的操作
class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        # 以0的位置为外循环,效率较低
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         nums[i]*=2
        #         nums[i+1]=0
        # i=0
        # k=0
        # while i<len(nums):
        #     if nums[i]==0:
        #         # j=i
        #         k=i+1
        #         while k<len(nums) and nums[k]==0:
        #             k+=1
        #         if k==len(nums):
        #             break
        #         temp=nums[k]
        #         nums[k]=nums[i]
        #         nums[i]=temp
        #     i+=1
        # return nums

        # 保留0的位置,到非零位置与之交换
        n = len(nums)
        j = 0
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
