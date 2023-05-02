# 给定三个整数 x 、 y 和 bound ，返回 值小于或等于 bound 的所有 强整数 组成的列表 。
# 如果某一整数可以表示为 xi + yj ，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个 强整数 。
# 你可以按 任何顺序 返回答案。在你的回答中，每个值 最多 出现一次。

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        a=0
        while x!=1 and pow(x,a)<=bound:
            a+=1
        b=0
        while y!=1 and pow(y,b)<=bound:
            b+=1
        print(a)
        print(b)
        ans=[]
        for i in range(a+1):
            for j in range(b+1):
                if pow(x,i)+pow(y,j)<=bound and pow(x,i)+pow(y,j) not in ans:
                    ans.append(pow(x,i)+pow(y,j))
        return ans

S=Solution()
print(S.powerfulIntegers(2,1,10))