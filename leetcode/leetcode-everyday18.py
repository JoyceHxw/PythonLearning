# 给定两个字符串 order 和 s 。order 的所有单词都是 唯一 的，并且以前按照一些自定义的顺序排序。
# 对 s 的字符进行置换，使其与排序的 order 相匹配。更具体地说，如果在 order 中的字符 x 出现字符 y 之前，那么在排列后的字符串中， x 也应该出现在 y 之前。
# 返回 满足这个性质的 s 的任意排列 。

from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # lst_o=list(order)
        # lst_s=list(s)
        # dic={l:lst_s.count(l) for l in lst_s}
        # lst_new=[]
        # for o in lst_o:
        #     if o in lst_s:
        #         if dic[o]==1:
        #             lst_new.append(o)
        #         if dic[o]>1:
        #             for i in range(0,dic[o]):
        #                 lst_new.append(o)
        # for s in lst_s:
        #     if s not in lst_new:
        #         for j in range(0,dic[s]):
        #             lst_new.append(s)
        # # print(lst_new)
        # s_new="".join(lst_new)
        # return s_new


        # 最简单的方法是直接对字符串 ss 进行排序。
        # 我们首先遍历给定的字符串 \textit{order}order，将第一个出现的字符的权值赋值为 11，第二个出现的字符的权值赋值为 22，以此类推。在遍历完成之后，所有未出现字符的权值默认赋值为 00。
        # 随后我们根据权值表，对字符串 ss 进行排序，即可得到一种满足要求的排列方案。

        val = defaultdict(int)
        for i, ch in enumerate(order):
            val[ch] = i + 1
        
        return "".join(sorted(s, key=lambda ch: val[ch]))
