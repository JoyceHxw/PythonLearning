# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。

from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # 双指针
        c=Counter(text)
        left=0
        right=0
        ans=1
        i=0
        while i<len(text):
            j=i
            while j<len(text) and text[i]==text[j]:
                j+=1
            left=j-i # 第一个子串的长度
            k=j+1
            while k<len(text) and text[i]==text[k]:
                k+=1
            right=k-j-1  # 第二个子串的长度
            print(left, " ", right)
            ans=max(ans,min(left+right+1,c[text[i]]))  # 是否有多余的字母可以替换
            i=j
        return ans

S=Solution()
print(S.maxRepOpt1("aaabaaa"))