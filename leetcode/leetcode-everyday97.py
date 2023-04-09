# 给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。
# 注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。


class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0 or n == 1:
            return str(n)
        res = []
        while n:
            # 计算当前 nn 的余数，由于当前的余数只能为 0 或 1，
            # 由于有符号整数均采用补码表示，最低位的奇偶性保持不变，
            # 因此可以直接取最低位即可，此时直接用 n&1 即可得到最低位的余数，将余数拼接到字符串的末尾。
            # 将 n 的值减去余数，然后将 n 的值除以 −2。
            remainder = n & 1
            res.append(str(remainder))
            n -= remainder
            # print(n)
            n //= -2
        return ''.join(res[::-1])
