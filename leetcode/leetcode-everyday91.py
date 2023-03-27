# 给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。换言之，请你找到 s 和 t 串中 恰好 只有一个字符不同的子字符串对的数目。
# 比方说， "computer" and "computation" 只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。
# 请你返回满足上述条件的不同子字符串对数目。
# 一个 子字符串 是一个字符串中连续的字符。


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # cnt=0
        # for i in range(1,min(len(s),len(t))+1):
        #     print("i=",i)
        #     for j in range(len(s)-i+1):
        #         for k in range(len(t)-i+1):
        #             diff=0
        #             for l in range(i):
        #                 print("l=",l)
        #                 print(s[j+l])
        #                 print(t[k+l])
        #                 if s[j+l]!=t[k+l]:
        #                     diff+=1
        #             if diff==1:
        #                 cnt+=1
        # return cnt

        ans = 0
        for i in range(len(s)):
            for j in range(len(t)):
                diff = 0
                k = 0
                # 利用已匹配的信息，只要diff<=1就继续判断
                while i + k < len(s) and j + k < len(t):
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        ans += 1
                    elif diff > 1:
                        break
                    k += 1
        return ans

S=Solution()
print(S.countSubstrings("ab","bb"))
