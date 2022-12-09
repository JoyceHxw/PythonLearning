# 给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。

# 我们可以将 n 转换成 3 进制。如果 n 的 3 进制表示中每一位均不为 2，那么答案为 True，否则为 False。

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            r=n%3
            if r==2:
                return False
            n=n//3
            print(n)
        if n==0:
            return True