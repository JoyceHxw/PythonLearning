class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # 暴力：求每个十进制数的二进制表达（短除法）
        for i in range(1,n+1):
            binary=""
            while i!=0:
                r=i%2
                i=int(i/2)
                binary=str(r)+binary
            print(binary)
            if binary not in s:
                return False
        return True
    
        # 逆向：枚举所有子字符串
        # seen = set()
        # s = list(map(int, s))  # 把 s[i] 全部转成 int
        # for i, x in enumerate(s):
        #     if x == 0: continue  # 二进制数从 1 开始，开头
        #     j = i + 1  # 下一个字符的下标
        #     while x <= n:
        #         print(x)
        #         seen.add(x)
        #         if j == len(s): break
        #         x = (x << 1) | s[j]  # 子串 s[i:j+1] 的二进制数
        #         j += 1
        # return len(seen) == n

S=Solution()
print(S.queryString("110101011011000011011111000000",15))