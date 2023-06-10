# 定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
# 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
# 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
# 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。

from collections import Counter

# 我的解法：暴力
# class Solution:
#     def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
#         words_fre=[]
#         for word in words:
#             c=Counter(word)
#             l=list(c.items())
#             l.sort(key=lambda x:x[0])
#             words_fre.append(l[0][1])
#         queries_fre=[]
#         for query in queries:
#             c=Counter(query)
#             l=list(c.items())
#             l.sort(key=lambda x:x[0])
#             queries_fre.append(l[0][1])
#         ans=[]
#         for i in range(len(queries)):
#             s=0
#             for j in range(len(words)):
#                 if queries_fre[i]<words_fre[j]:
#                     s+=1
#             ans.append(s)
#         return ans


# 答案：后缀和
# 注意求最小字符的出现次数的方法
class Solution:
    def f(self, s: str) -> int:
        cnt = 0
        ch = 'z'
        for c in s:
            if c < ch:
                ch = c
                cnt = 1
            elif c == ch:
                cnt += 1
        return cnt

    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        count = [0] * 12
        for s in words:
            # 最小字符的出现次数对应数组的下标，统计个数
            count[self.f(s)] += 1
        # 后缀和（因为是从小到大排序，需要统计大于的个数）
        for i in range(9, 0, -1):
            count[i] += count[i + 1]
        res = []
        for s in queries:
            res.append(count[self.f(s) + 1])
        return res
