# 给你一个数组 nums ，数组中只包含非负整数。定义 rev(x) 的值为将整数 x 各个数字位反转得到的结果。比方说 rev(123) = 321 ， rev(120) = 21 。我们称满足下面条件的下标对 (i, j) 是 好的 ：
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# 请你返回好下标对的数目。由于结果可能会很大，请将结果对 109 + 7 取余 后返回。

# class Solution:
#     def countNicePairs(self, nums: list[int]) -> int:
#         r_lst=[]
#         for num in nums:
#             num_s=str(num)
#             r=""
#             if len(num_s)==1:
#                 r='0'
#             else:
#                 for i in range(int(len(num_s)/2)):
#                     a=int(num_s[i])
#                     b=int(num_s[len(num_s)-i-1])
#                     r+=str(abs(a-b))
#             r_lst.append([num,int(r)])
#         print(r_lst)
#         cnt=0
#         for i in range(len(r_lst)):
#             for j in range(i+1,len(r_lst)):
#                 if r_lst[i][1]==r_lst[j][1]:
#                     cnt+=1
#         return cnt


from collections import Counter


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        res = 0
        cnt = Counter()  # 用来统计一个 python 列表、字符串、元组等可迭代对象中每个元素出现的次数，并返回一个字典
        for i in nums:
            print("i=",i)
            j = int(str(i)[::-1])
            print("j=",j)
            print(cnt[i - j])
            res += cnt[i - j]
            print("res=",res)
            cnt[i - j] += 1
        return res % (10 ** 9 + 7)

S=Solution()
# print(S.countNicePairs([352171103,442454244,42644624,152727101,413370302,293999243]))
# print(S.countNicePairs([42,11,1,97]))
# print(S.countNicePairs([432835222,112141211,5408045,456281503,283322436,414281561,37773,286505682]))
print(S.countNicePairs([442111244,357716602,131050131,251794140,4046404,373969224,1082801,468525864,384140537,492968345]))  # 原算法错误