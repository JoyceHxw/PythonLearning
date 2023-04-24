# 给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
class Solution:
    def lastSubstring(self, s: str) -> str:
        # 双指针
        max_l=s[0]
        max_p=0
        # 超出时间限制，中间有些判断是多余的
        # 先判断当前字母是不是较大，如果相等，继续判断后面的字母
        # for i in range(1,len(s)):
        #     if s[i]>max_l:
        #         max_l=s[i]
        #         max_p=i
        #     elif s[i]==max_l:
        #         print("i=",i)
        #         for j in range(1,len(s)-i):
        #             print("111111",s[i+j])
        #             print("222222",s[max_p+j])
        #             if s[i+j]>s[max_p+j]:
        #                 max_p=i
        #                 break
        #             elif s[i+j]<s[max_p+j]:
        #                 break
        i=1
        while i<len(s):
            k=0 # 包括了比对字符串的首字母
            while i+k<len(s) and s[i+k]==s[max_p+k]:
                k+=1
            if i+k<len(s) and s[i+k]>s[max_p+k]:
                max_p,i=i,max(i+1,max_p+k+1)
            else:
                i=i+k+1
                        
        return s[max_p:]

S=Solution()
# print(S.lastSubstring("cacacb"))
print(S.lastSubstring("zzwobllyxktqeibfoupcpptncggrdqbkji"))
# "zzwobllyxktqeibfoupcpptncggrdqbkji"
# yxktqeibfoupcpptncggrdqbkji