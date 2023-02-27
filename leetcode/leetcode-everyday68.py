# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。

# 如果符合下列情况之一，则数组 A 就是 锯齿数组：

# 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
# 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 返回将数组 nums 转换为锯齿数组所需的最小操作次数。


# 只能减小，不能增加
class Solution:
    def movesToMakeZigzag(self, nums: list[int]) -> int:
        lst=[]
        for j in (0,1):
            s=0
            # 满足奇数位大，只能对偶数位进行操作（只能减小）
            # 满足奇数位小，只能对奇数位进行操作（只能减小）
            # 当j=0，对偶数位进行操作
            # 当j=1，对奇数位进行操作
            for i in range(j,len(nums),2):
                if i==len(nums)-1:
                    s+=max(nums[i]-nums[i-1]+1,0)
                elif i==0:
                    s+=max(nums[i]-nums[i+1]+1,0)
                else:
                    s+=max(nums[i]-nums[i+1]+1,nums[i]-nums[i-1]+1,0)
            lst.append(s)
        return min(lst)

S=Solution()
# print(S.movesToMakeZigzag([2,7,10,9,8,9]))
# print(S.movesToMakeZigzag([9,6,1,6,2]))
# print(S.movesToMakeZigzag([7,4,8,9,7,7,5]))
print(S.movesToMakeZigzag([3,10,7,9,9,3,6,9,4]))