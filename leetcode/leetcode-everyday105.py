from bisect import bisect_left
from cmath import inf


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        # 算法错误，从左到右每一步纠正顺序并不是最优的
        # arr2.sort()
        # j=0
        # cnt=0
        # i=0
        # while i<len(arr1)-1:
        #     print(arr1)
        #     m=i
        #     while arr1[i]>=arr1[i+1]:
        #         # print(arr1[i])
        #         # 替换当前节点和下一节点
        #         # print("m=",m)
        #         if m==0:
        #             if arr2[0]<arr1[i+1]:
        #                 cnt+=1
        #                 arr1[0]=arr2[0]                       
        #             else:
        #                 return -1
        #         else:
        #             while j<len(arr2) and arr2[j]<=arr1[m-1]:
        #                 j+=1
        #             if j==len(arr2):
        #                 return -1
        #             else:
        #                 if arr2[j]==arr1[m]:
        #                     pass
        #                 else:
        #                     cnt+=1
        #                     arr1[m]=arr2[j]

        #         m+=1
        #     i+=1
        # return cnt

        # dp?????????????
        a = arr1 + [inf]  # 简化代码逻辑
        b = sorted(set(b))  # 去重+排序
        n = len(a)  # 注意 a 已经添加了一个元素
        f = [0] * n  # 这里初始化成任何值都行
        for i, x in enumerate(a):
            k = bisect_left(b, x) # bisect_left返回大于等于x的第一个下标
            res = 0 if k >= i else -inf  # 小于 a[i] 的数全部替换
            if i and a[i - 1] < x:  # 无替换
                res = max(res, f[i - 1])
            for j in range(i - 2, max(i - k - 2, -1), -1):
                if b[k - (i - j - 1)] > a[j]:
                    # a[j+1] 到 a[i-1] 替换成 b[k-(i-j-1)] 到 b[k-1]
                    res = max(res, f[j])
            f[i] = res + 1  # 把 +1 移到这里，表示 a[i] 不替换
        return -1 if f[-1] < 0 else n - f[-1]  # 注意 a 已经添加了一个元素

                    
S=Solution()
# print(S.makeArrayIncreasing([1,5,3,6,7],[4,3,1]))
# print(S.makeArrayIncreasing([1,5,3,6,7],[1,6,3,3]))  # arr2元素不能改变，
# print(S.makeArrayIncreasing([0,11,6,1,4,3],[5,4,11,10,1,0]))
print(S.makeArrayIncreasing([5,16,19,2,1,12,7,14,5,16],[6,17,4,3,6,13,4,3,18,17,16,7,14,1,16]))

