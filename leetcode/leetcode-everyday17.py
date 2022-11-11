# 给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。
# 两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。
# 如果 a 和 b 相似，返回 true ；否则，返回 false 。

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # lst=[]
        # lst_check=['a','e','i','o','u','A','E','I','O','U']
        # for l in s:
        #     lst.append(l)
        # m=int(len(lst)/2)
        # lst1=lst[:m]
        # lst2=lst[m:]
        # cnt1=0
        # cnt2=0
        # for l1 in lst1:
        #     if l1 in lst_check:
        #         cnt1+=1
        # for l2 in lst2:
        #     if l2 in lst_check:
        #         cnt2+=1
        
        # return cnt1==cnt2

        VOWELS = "aeiouAEIOU"
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        return sum(c in VOWELS for c in a) == sum(c in VOWELS for c in b)
