# 给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。
# 字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # dp 从第一个开始推，第一个限制最小
        # n为2，a: 5, e: 4, i: 3, o: 2, u: 1
        # n为3，a: 5+4+3+2+1, e: 4+3+2+1, i:3+2+1, o:2+1, u:1   
        # n为4，a: 15+10+6+3+1, e: 10+6+3+1, i: 6+3+1, o: 3+1, u:1
        cnts=[1]*5
        if n==1:
            return sum(cnts)
        else:
            for i in range(1,n):
                s=[]
                for j in range(5):
                    s.append(sum(cnts[j:]))
                cnts=s
            return sum(cnts)