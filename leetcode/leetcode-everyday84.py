class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # 超出时间限制
        # for i in range(-1,len(a)+1):
        #     s1=""
        #     s2=""
        #     if i==-1:
        #         s1=b
        #         s2=a
        #     elif i==len(a):
        #         s1=a
        #         s2=b
        #     else:
        #         s1=a[:i+1]+b[i+1:]
        #         s2=b[:i+1]+a[i+1:]
        #     print(s1)
        #     print(s2)
        #     isEqual1=True
        #     isEqual2=True
        #     for j in range(0,int(len(a)/2)):
        #         # print("j=",j)
        #         if s1[j]!=s1[len(a)-j-1]:
        #             isEqual1=False
        #             break
        #     for j in range(0,int(len(a)/2)):
        #         print("j=",j)
        #         if s2[j]!=s2[len(a)-j-1]:
        #             isEqual2=False
        #             break
        #     if isEqual1==True or isEqual2==True:
        #         return True
        # return False

        # 双指针
        # 如果 a_prefix + b_suffix 可以构成回文串则返回 True，否则返回 False
        def check(a: str, b: str) -> bool:
            i, j = 0, len(a) - 1  # 相向双指针
            while i < j and a[i] == b[j]:  # 前后缀尽量匹配
                i += 1
                j -= 1
            print("i=",i)
            print("j=",j)
            s, t = a[i: j + 1], b[i: j + 1]  # 中间剩余部分
            print(s)
            print(t)
            print(s[::-1])
            return s == s[::-1] or t == t[::-1]  # 判断是否为回文串
        return check(a, b) or check(b, a)

S=Solution()
# print(S.checkPalindromeFormation("xbdef","xecab"))
# print(S.checkPalindromeFormation("abda","acmc"))
# print(S.checkPalindromeFormation("ulacfd","jizalu"))
print(S.checkPalindromeFormation("abcaabaaaa","aaabdbacba"))