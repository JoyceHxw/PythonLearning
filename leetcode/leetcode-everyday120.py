# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
# 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        # if len(barcodes)==1:
        #     return barcodes
        # ans=[]
        # c=Counter(barcodes)
        # i=0
        # while i<len(barcodes):
        #     # 选择最多的两个
        #     # 每次排序超出时间限制
        #     c_s=sorted(c.items(),key=lambda x:x[1], reverse=True)
        #     j=0
        #     while j<2:
        #         if c_s[j][1]!=0:
        #             ans.append(c_s[j][0])
        #             i+=1
        #             c[c_s[j][0]]-=1
        #         j+=1
        # return ans
        
        # 逆向思维，顺序不变，改变插入位置
        c=Counter(barcodes)
        barcodes.sort(key=lambda x: (-c[x], x))
        ans = [0] * len(barcodes)
        ans[::2] = barcodes[: (len(barcodes) + 1) // 2]
        ans[1::2] = barcodes[(len(barcodes) + 1) // 2:]
        return ans

S=Solution()
print(S.rearrangeBarcodes([1,1,1,1,2,2,3,3]))