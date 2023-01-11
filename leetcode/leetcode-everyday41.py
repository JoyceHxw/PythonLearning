# 给你一个下标从 0 开始长度为 n 的字符串 num ，它只包含数字。
# 如果对于 每个 0 <= i < n 的下标 i ，都满足数位 i 在 num 中出现了 num[i]次，那么请你返回 true ，否则返回 false 。

class Solution:
    def digitCount(self, num: str) -> bool:
        is_flag=True
        for i in range(0,len(num)):
            print(num[i])
            print(num.count(str(i)))
            if int(num[i])==num.count(str(i)):
                is_flag=True
            else:
                return False
        return is_flag

S=Solution()
print(S.digitCount("1210"))