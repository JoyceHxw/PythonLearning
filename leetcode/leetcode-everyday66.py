# 给你一个非负整数数组 nums 。在一步操作中，你必须：

# 选出一个正整数 x ，x 需要小于或等于 nums 中 最小 的 非零 元素。
# nums 中的每个正整数都减去 x。
# 返回使 nums 中所有元素都等于 0 需要的 最少 操作数。


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # m=max(nums)
        # nums.sort()
        # a=0
        # s=0
        # cnt=0
        # number=[]
        # if m==0:
        #     return 0
        # else:
        #     for n,i in enumerate(nums):
        #         a=i-s
        #         s+=a
        #         if i ==0:
        #             pass
        #         elif i not in number:
        #             m-=a
        #             cnt+=1
        #             number.append(i)
        #             if m==0:
        #                 return cnt
        return len({x for x in nums if x})   # 直接统计非零的不同元素

                    
S=Solution()
# print(S.minimumOperations([1]))
print(S.minimumOperations([1,1,1,2,2,2,3,3]))