# 给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。
# 返回 n 的长度。如果不存在这样的 n ，就返回-1。

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        a=1
        # r=[] 时间比set多，会超出时间限制，改成集合
        r=set()
        cnt=1
        while a%k!=0:
            print(a%k)
            if a%k not in r:
                r.add(a%k)
                a=10*a+1
                cnt+=1
            else:
                break
        if a%k==0:
            return cnt
        else:
            return -1
        
        # x % k = r 则（10x + 1) % k = (10(nk + r) + 1) % k = (10r + 1) % k
        # 减少数位
        # n = 1 % k
        # for i in range(1, k + 1):
        #     if n == 0:
        #         return i
        #     n = (n * 10 + 1) % k
        # return -1。

S=Solution()
print(S.smallestRepunitDivByK(49993))