# 给你一个由英文字母组成的字符串 s ，请你找出并返回 s 中的 最好 英文字母。返回的字母必须为大写形式。如果不存在满足条件的字母，则返回一个空字符串。
# 最好 英文字母的大写和小写形式必须 都 在 s 中出现。
# 英文字母 b 比另一个英文字母 a 更好 的前提是：英文字母表中，b 在 a 之 后 出现。

class Solution:
    def greatestLetter(self, s: str) -> str:
        s=set(s)
        s=sorted(s,reverse=True)
        print(s)
        for i in s:
            if i.islower():
                if i.upper() in s:
                    return i.upper()
            else:
                return ""
        return ""

S=Solution()
print(S.greatestLetter("AbCdEfGhIjK"))