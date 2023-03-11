# 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。
# 返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。


from itertools import accumulate


class Solution:
    def findLongestSubarray(self, array: list[str]) -> list[str]:
        # lst=[]
        # # 把字母和数字换成1，-1方便计算
        # for i in array:
        #     if i.isdigit():
        #         lst.append(1)
        #     else:
        #         lst.append(-1)
        # # print(lst)
        # # 前缀和
        # h={}
        # max_lenth=0
        # r_left=0
        # r_right=0
        # s = list(accumulate(lst, initial=0))
        # for i, v in enumerate(s):
        #     h.setdefault(v,[]).append(i)
        #     j=min(h[v])
        #     if max_lenth<i-j:  #如果加等号，会把后面长度相等，但左坐标大的考虑进来
        #         r_left=j
        #         r_right=i
        #         max_lenth=i-j
        # return array[r_left:r_right]
    
        # 简化代码
        s = list(accumulate((-1 if v[0].isdigit() else 1 for v in array), initial=0))
        begin = end = 0  # 符合要求的子数组 [begin,end)
        first = {}
        for i, v in enumerate(s):
            j = first.get(v, -1)  # 没有则返回-1
            if j < 0:  # 首次遇到 s[i]，即为最小值
                first[v] = i
            elif i - j > end - begin:  # 更长的子数组
                begin, end = j, i
        return array[begin:end]
    
S=Solution()
print(S.findLongestSubarray(["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]))