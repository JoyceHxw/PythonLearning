# 给你一个下标从 0 开始的字符串 s ，该字符串仅由小写英文字母组成，s 中的每个字母都 恰好 出现 两次 。另给你一个下标从 0 开始、长度为 26 的的整数数组 distance 。
# 字母表中的每个字母按从 0 到 25 依次编号（即，'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25）。
# 在一个 匀整 字符串中，第 i 个字母的两次出现之间的字母数量是 distance[i] 。如果第 i 个字母没有在 s 中出现，那么 distance[i] 可以 忽略 。
# 如果 s 是一个 匀整 字符串，返回 true ；否则，返回 false 。

class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        # d={}
        # for i in range(len(s)):
        #     # print(ord(s[i]))
        #     j=distance[ord(s[i])-97]
        #     k=i+1
        #     if d.get(s[i],-1)==-1:
        #         if j+i+1<len(s) and s[i]!=s[j+i+1]:
        #             return False
        #         while k<=j+i and k<len(s):
        #             if s[k]==s[i]:
        #                 return False
        #             k+=1
        #         d[s[i]]=1
        #     else:
        #         d[s[i]]+=1
        # return True

        # 简化代码
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j] and distance[ord(s[i]) - ord('a')] != j - i - 1:
                    return False
        return True
