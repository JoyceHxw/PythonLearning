# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result=[]
        for i,l in enumerate(nums):
            k=target-l
            for j,a in enumerate(nums[i+1:]):
                if a==k and j+i+1!=i and j+i+1 not in result and i not in result:
                    result.append(i)
                    result.append(j+i+1)
        return result

S=Solution()
# print(S.twoSum([0,4,3,0],0))
print(S.twoSum([-1,-2,-3,-4,-5],-8))