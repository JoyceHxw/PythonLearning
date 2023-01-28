# 给你一个整数数组 nums 。你需要选择 恰好 一个下标（下标从 0 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。

# 比方说，如果 nums = [6,1,7,4,1] ，那么：

# 选择删除下标 1 ，剩下的数组为 nums = [6,7,4,1] 。
# 选择删除下标 2 ，剩下的数组为 nums = [6,1,4,1] 。
# 选择删除下标 4 ，剩下的数组为 nums = [6,1,7,4] 。
# 如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 平衡数组 。

# 请你返回删除操作后，剩下的数组 nums 是 平衡数组 的 方案数 。


# 超出时间限制
# class Solution:
#     def waysToMakeFair(self, nums: list[int]) -> int:
#         cnt=0
#         for i in range(len(nums)):
#             nums_d=nums[:]  # 不指向同一个地址
#             nums_d.pop(i)
#             if sum(nums_d[0::2])==sum(nums_d[1::2]):
#                 cnt+=1
#         return cnt


class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        s1, s2 = sum(nums[::2]), sum(nums[1::2])
        print("偶数下标元素和s1=",s1)
        print("奇数下标元素和s2=",s2)
        ans = t1 = t2 = 0
        for i, v in enumerate(nums):
            print("t1=",t1)
            print("t2=",t2)
            ans += i % 2 == 0 and t2 + s1 - t1 - v == t1 + s2 - t2  # 当删除下标为偶数
            ans += i % 2 == 1 and t2 + s1 - t1 == t1 + s2 - t2 - v
            t1 += v if i % 2 == 0 else 0  # 已遍历的偶数和
            t2 += v if i % 2 == 1 else 0
        return ans

S=Solution()
print(S.waysToMakeFair([2,1,6,4]))