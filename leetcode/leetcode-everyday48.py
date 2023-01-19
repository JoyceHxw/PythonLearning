# 如果一个密码满足以下所有条件，我们称它是一个 强 密码：
# 它有至少 8 个字符。
# 至少包含 一个小写英文 字母。
# 至少包含 一个大写英文 字母。
# 至少包含 一个数字 。
# 至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。
# 它 不 包含 2 个连续相同的字符（比方说 "aab" 不符合该条件，但是 "aba" 符合该条件）。
# 给你一个字符串 password ，如果它是一个 强 密码，返回 true，否则返回 false 。


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        is_flag1=False
        is_flag2=False
        is_flag3=False
        is_flag4=False
        for l in password:
            if len(password)<8:
                return False
            if l.isupper():
                is_flag1=True
            if l.islower():
                is_flag2=True
            if l.isdigit():
                is_flag3=True
            if l in "!@#$%^&*()-+":
                is_flag4=True
            if password.index(l)<len(password)-1:
                if l==password[password.index(l)+1]:
                    return False

        return is_flag1 and is_flag2 and is_flag3 and is_flag4
S=Solution()
print(S.strongPasswordCheckerII("11A!A!Aa"))