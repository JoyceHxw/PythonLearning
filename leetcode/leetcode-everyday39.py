# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

# class Solution:
#     def minOperations(self, nums: list[int], x: int) -> int:
#         cnt=0
#         while x>0:
#             if len(nums)>=2:
#                 if nums[0]>=nums[-1]:
#                     if x>=nums[0]:
#                         x-=nums[0]
#                         nums.pop(0)
#                         cnt+=1
#                     elif x>=nums[-1]:
#                         x-=nums[-1]
#                         nums.pop(-1)
#                         cnt+=1
#                     else:
#                         return -1
#                 else:
#                     if x>=nums[-1]:
#                         x-=nums[-1]
#                         nums.pop(-1)
#                         cnt+=1
#                     elif x>=nums[0]:
#                         x-=nums[0]
#                         nums.pop(0)
#                         cnt+=1
#                     else:
#                         return -1
#             else:
#                 if sum(nums)==x:
#                     cnt+=1
#                     return cnt
#                 else:
#                     return -1
#         return cnt


# 把问题转换成「从 nums 中移除一个最长的子数组，使得剩余元素的和为 x」。
# 换句话说，要从 nums 中找最长的子数组，其元素和等于 s−x，这里 s 为 nums 所有元素之和。
# 注：我一般把窗口大小不固定的叫做双指针，窗口大小固定的叫做滑动窗口。
# 最后答案为 nums 的长度减去最长子数组的长度。

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        print('target=',target)
        if target < 0: 
            return -1  # 全部移除也无法满足要求
        ans = -1
        left = s = 0
        for right, x in enumerate(nums):
            s += x
            print(s)
            while s > target:  # 缩小子数组长度
                print("循环")
                s -= nums[left]
                print(s)
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
                print("ans=",ans)
        return -1 if ans < 0 else len(nums) - ans


S=Solution()
print(S.minOperations([3,2,20,1,1,3],10))