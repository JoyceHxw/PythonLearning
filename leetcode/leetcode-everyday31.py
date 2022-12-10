class Solution:
    def maxHeight(self, cuboids: list[list[int]]) -> int:
        # 第一个不一定作为底层箱子
        # for cube in cuboids:
        #     cube.sort()
        # cuboids.sort(key=lambda x:x[2],reverse=True)
        # h=cuboids[0][2]
        # print(cuboids)
        # j=0
        # for i in range(1,len(cuboids)):
        #     if cuboids[j][0]>=cuboids[i][0] and cuboids[j][1]>=cuboids[i][1] and cuboids[j][2]>=cuboids[i][2]:
        #         h+=cuboids[i][2]
        #         j=i
            
        # return h

        # 每个箱子都作为底层进行计算 
        for c in cuboids:
            c.sort()
        cuboids.sort()
        print(cuboids)
        f = [0] * len(cuboids)
        print(f)
        for i, (_, l2, h2) in enumerate(cuboids):
            print("i=",i)
            for j, (_, l1, h1) in enumerate(cuboids[:i]):
                print("j=",j)
                if l1 <= l2 and h1 <= h2:  # 排序后，w1 <= w2 恒成立
                    print("f[i]=",f[i])
                    print("f[j]=",f[j])
                    f[i] = max(f[i], f[j])  # cuboids[j] 可以堆在 cuboids[i] 上
            f[i] += h2
            print("f[i]=",f[i])
        return max(f)


S=Solution()
# print(S.maxHeight([[38,25,45],[76,35,3]]))
# print(S.maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))
# print(S.maxHeight([[36,46,41],[15,100,100],[75,91,59],[13,82,64]]))
print(S.maxHeight([[50,26,84],[2,55,62],[64,63,72]]))   # 原做法不成立