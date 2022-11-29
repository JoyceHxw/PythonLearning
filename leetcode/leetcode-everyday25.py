# 给你一个仅由字符 '0' 和 '1' 组成的字符串 s 。一步操作中，你可以将任一 '0' 变成 '1' ，或者将 '1' 变成 '0' 。
# 交替字符串 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。例如，字符串 "010" 是交替字符串，而字符串 "0100" 不是。
# 返回使 s 变成 交替字符串 所需的 最少 操作数。

class Solution:
    def minOperations(self, s: str) -> int:
        # lst=list(s)
        # lst0=list(map(int,lst))
        # lst1=[]
        # lst2=[]
        # for n in range(len(lst0)):
        #     if n%2 == 0:
        #         lst1.append(1)
        #         lst2.append(0)
        #     else:
        #         lst1.append(0)
        #         lst2.append(1)
        # cnt1=0
        # cnt2=0
        # for i in range(len(lst0)):
        #     if lst0[i]!=lst1[i]:
        #         cnt1+=1
        #     if lst0[i]!=lst2[i]:
        #         cnt2+=1
        # return min(cnt1,cnt2)
        
        # 注意到，变成这两种不同的交替二进制字符串所需要的最少操作数加起来等于 s 的长度，我们只需要计算出变为其中一种字符串的最少操作数，就可以推出另一个最少操作数，然后取最小值即可。
        cnt = sum(int(c) != i % 2 for i, c in enumerate(s))
        for i,c in enumerate(s):
            print(i)
            print(c)
            print(int(c) != i % 2)
        print(cnt)
        return min(cnt, len(s) - cnt)

S=Solution()
S.minOperations("0100")
