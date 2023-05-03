# 给你一个字符串 s ，请你判断它是否 有效 。
# 字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ：
# 将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 tleft + "abc" + tright，其中 t == tleft + tright 。注意，tleft 和 tright 可能为 空 。
# 如果字符串 s 有效，则返回 true；否则，返回 false。


from collections import Counter


class Solution:
    def isValid(self, s: str) -> bool:
        # 栈 类似于括号
        stack=[]
        for i in range(len(s)):
            if s[i]=='a' or s[i]=='b':
                stack.append(s[i])
            else:
                if len(stack)>=2 and stack[-1]=='b' and stack[-2]=='a':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            print(stack)
        if stack==[]:
            return True
        else:
            return False

S=Solution()
# print(S.isValid("abcabcababcc"))
# print(S.isValid("aabcbabcc"))
# print(S.isValid("aabcbcabc"))
# print(S.isValid("aaababccbcbc"))
# print(S.isValid("abccba"))
print(S.isValid("aabcbc"))